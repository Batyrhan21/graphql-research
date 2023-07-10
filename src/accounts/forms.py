from typing import Any
from PIL import Image

from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm

from common.utils import compress_image
from accounts import models


class UserImageCompressForm(UserChangeForm):
    photo = forms.ImageField(required=False)

    class Meta:
        model = models.User
        fields = ["photo"]

    def save(self, commit=True) -> Any:
        instance = super(UserImageCompressForm, self).save(commit=False)
        if "photo" in self.changed_data:
            photo = self.cleaned_data.get("photo")
            if photo:
                instance.photo = compress_image(
                    photo, is_small_thumbnail=True, quality=80
                )
            else:
                instance.photo = None
        if commit:
            instance.save()
        return instance

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if photo:
            try:
                Image.open(photo)
            except:
                raise forms.ValidationError("Invalid image file")
        return photo

