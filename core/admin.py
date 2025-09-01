from django.contrib import admin
from .models import Property, PropertyAddress, PropertyImage, PGDetails

class AddressInline(admin.StackedInline):
    model = PropertyAddress
    extra = 0

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PGDetailsInline(admin.StackedInline):
    model = PGDetails
    extra = 0

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "category", "property_type", "price", "created_at")
    list_filter = ("category", "property_type", "created_at")
    search_fields = ("title", "description", "owner__email")
    inlines = [PropertyImageInline, PGDetailsInline]

@admin.register(PropertyAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("address_line", "city", "state", "pincode", "latitude", "longitude")
    search_fields = ("city", "state", "pincode")

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("property", "image")

@admin.register(PGDetails)
class PGDetailsAdmin(admin.ModelAdmin):
    list_display = ("property", "for_gender", "room_type", "max_rent", "wifi", "food", "ac")
    list_filter = ("for_gender", "room_type", "wifi", "food", "ac", "parking")
