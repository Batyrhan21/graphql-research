from django.contrib import admin

from common.mixins import ImageTagMixin
from common.forms import GeneralCompressImageForm

class BaseTabularInline(admin.TabularInline, ImageTagMixin):
    min_num = 1
    extra = 1
    max_num = 5
    form = GeneralCompressImageForm
    verbose_name_plural = "Изображения"
    verbose_name = "Изображение"