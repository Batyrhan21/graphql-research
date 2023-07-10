from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from product import models, inlines
from common.admin import BaseAdmin 


@admin.register(models.Product)
class ProductAdmin(BaseAdmin):
    list_display = ["title", "description", "category"]
    list_filter = ["category", "is_deleted"]
    search_fields = ["title", "description", "category__title"]
    empty_value_display = _("Empty")
    inlines = (inlines.ProductImageInline,)
    fieldsets = (
        (
            _("General"),
            {
                "fields": (
                    "title",
                    "description",
                    "category",
                )
            },
        ),
    ) + BaseAdmin.fieldsets if BaseAdmin.fieldsets else () 


@admin.register(models.Category)
class CategoryAdmin(BaseAdmin):
    list_display = ["title"]
    list_filter = ["is_deleted"]
    search_fields = ["title"]
    empty_value_display = _("Empty")
    fieldsets = (
        (
            _("General"),
            {
                "fields": (
                    "title",
                )
            },
        ),
    ) + BaseAdmin.fieldsets if BaseAdmin.fieldsets else () 