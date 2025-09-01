from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class PropertyAddress(models.Model):
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.address_line}, {self.city} - {self.pincode}"


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('rent', 'Rent'),
        ('buy', 'Buy'),
        ('sell', 'Sell'),
        ('pg', 'PG'),
    ]
    CATEGORY_CHOICES = [
        ('room', 'Room'),
        ('flat', 'Flat'),
        ('plot', 'Plot'),
        ('commercial', 'Commercial'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    address = models.OneToOneField(PropertyAddress, on_delete=models.CASCADE, related_name="property")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.property_type})"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return f"Image for {self.property.title}"


# 🔹 New PG Details
class PGDetails(models.Model):
    GENDER_CHOICES = [
        ("boys", "Boys"),
        ("girls", "Girls"),
        ("both", "Both"),
    ]
    ROOM_TYPE_CHOICES = [
        ("private", "Private Room"),
        ("double", "Double Sharing"),
        ("triple", "Triple Sharing"),
    ]
    property = models.OneToOneField("Property", on_delete=models.CASCADE, related_name="pg_details")
    for_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    wifi = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    housekeeping = models.BooleanField(default=False)
    max_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PG ({self.for_gender} - {self.room_type})"
