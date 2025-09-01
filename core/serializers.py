from rest_framework import serializers
from .models import Property, PropertyImage, PropertyAddress, PGDetails


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ["id", "image"]


class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = ["id", "address_line", "city", "state", "pincode", "latitude", "longitude"]


class PGDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGDetails
        fields = [
            "for_gender", "sharing_type",
            "wifi", "food", "laundry", "tv", "ac", "parking", "housekeeping"
        ]


class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    address = PropertyAddressSerializer()
    pg_details = PGDetailsSerializer(required=False)

    class Meta:
        model = Property
        fields = [
            "id", "title", "description", "property_type", "category",
            "price", "address", "pg_details", "created_at", "images", "uploaded_images"
        ]

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        pg_data = validated_data.pop("pg_details", None)
        uploaded_images = validated_data.pop("uploaded_images", [])

        address = PropertyAddress.objects.create(**address_data)
        property_obj = Property.objects.create(address=address, **validated_data)

        for img in uploaded_images:
            PropertyImage.objects.create(property=property_obj, image=img)

        if property_obj.property_type == "pg" and pg_data:
            PGDetails.objects.create(property=property_obj, **pg_data)

        return property_obj
