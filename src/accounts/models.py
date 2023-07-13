from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True,
        verbose_name=_("Login"),
        help_text=_("Enter Latin only"),
    )
    password = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("Password"),
    )
    full_name = models.CharField(
        blank=False,
        null=False,
        max_length=250,
        verbose_name=_("ФИО"),
        help_text=_("Enter only the full name"),
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name=_("First name"),
        help_text=_("Enter only the first name"),
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name=_("Last name"),
        help_text=_("Enter only the last name"),
    )
    photo = models.ImageField(
        _("Photo"), upload_to="user_media/%Y/%m/%d/", null=True, blank=True
    )
    phone = models.CharField(
        blank=True,
        null=True,
        max_length=150,
        verbose_name=_("Phone number"),
        help_text=_("Enter phone number"),
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_("E-mail"),
        help_text=_("Enter email"),
    )
    is_staff = models.BooleanField(default=False, verbose_name=_("Is staff"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_("Is superuser"),
        help_text=_("Has access to the administrator panel"),
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "users__users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ("-created_at",)

