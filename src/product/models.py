from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from common.models import BaseModel


class ImageProductModel(BaseModel):
    image = models.ImageField(
        blank=False,
        null=False,
        upload_to="product/image/%Y/%m/%d",
        verbose_name=_("Изображения продукта"),
        validators=[
            FileExtensionValidator(
                allowed_extensions=["png", "jpg", "jpeg", "jpg", "webp"]
            )
        ],
    )
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Продукт"),
        related_name="product_images",
    )

    def __str__(self) -> str:
        return str(f"{self.product.title}'s image")

    class Meta:
        db_table = "product__product_image"
        verbose_name = _("Изображения продукта")
        verbose_name_plural = _("Изображения продукта")


class Category(BaseModel):
    title = models.CharField(
        null=False, blank=False, max_length=155, verbose_name=_("Заголовок")
    )

    def __str__(self) -> str:
        return str(f"Category: {self.title}")

    class Meta:
        db_table = "product__category"
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class Product(BaseModel):
    title = models.CharField(
        null=False, blank=False, max_length=155, verbose_name=_("Заголовок")
    )
    description = models.TextField(
        null=True, blank=True, max_length=255, verbose_name=_("Описание")
    )
    category = models.ForeignKey(
        "product.Category",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Категория"),
        related_name="products",
    )

    def __str__(self) -> str:
        return str(f"Product: {self.title}")

    class Meta:
        db_table = "product__product"
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")
