from django.contrib import admin

from product import models



class ProductImageInline(admin.TabularInline):
    model = models.ImageProductModel
    fields = [
        "image",
    ]
    extra = 1