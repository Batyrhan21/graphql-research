from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.apps import apps

from common.mixins import PhotoTagAdminMixin
from accounts import models, forms


app = apps.get_app_config("graphql_auth")
for model_name, model in app.models.items():
    admin.site.register(model)


@admin.register(models.User)
class UserAdmin(UserAdmin, PhotoTagAdminMixin):
    list_display = (
        "photo_tag",
        "username",
        "full_name",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "photo_tag",
        "username",
    )
    list_editable = ("is_staff",)
    search_fields = ("username", "email", "full_name", "phone")
    list_filter = ("is_deleted", "is_superuser")
    readonly_fields = ("created_at", "id", "updated_at")
    ordering = ("-created_at", "username")
    list_per_page = 20
    form = forms.UserImageCompressForm
    PhotoTagAdminMixin.photo_tag.short_description = "Photo"
    fieldsets = (
        (
            _("General"),
            {
                "fields": (
                    "photo",
                    "username",
                    "password",
                    "full_name",
                    "email",
                    "phone",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "is_deleted",
                )
            },
        ),
        (_("Dates"), {"fields": ("created_at",)}),
    )
