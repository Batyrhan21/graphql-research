from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


admin.site.unregister(Group)


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)
    list_per_page = 20
    fieldsets = (
        (
            _("Permissions"),
            {
                "fields": (
                    "is_deleted",
                )
            },
        ),
        (_("Dates"), {"fields": ("created_at", "updated_at")}),
    )