from django import forms

from common.utils import compress_image


class ImageField(forms.FileField):
    def __init__(
        self,
        *,
        quality=50,
        max_length=None,
        allow_empty_file=False,
        is_small_thumbnail=False,
        is_medium_thumbnail=False,
        is_big_thumbnail=False,
        is_extra_small=False,
        **kwargs,
    ):
        self.max_length = max_length
        self.quality = quality
        self.is_small_thumbnail = is_small_thumbnail
        self.is_medium_thumbnail = is_medium_thumbnail
        self.is_big_thumbnail = is_big_thumbnail
        self.is_extra_small = is_extra_small
        self.allow_empty_file = allow_empty_file
        super().__init__(**kwargs)


class BaseModelForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(BaseModelForm, self)
        if instance:
            instance = super(BaseModelForm, self).save(commit=False)
            for field in self.__class__.declared_fields:
                if (
                    field in self.changed_data
                    and self.cleaned_data[f"{field}"] is not False
                ):
                    setattr(
                        instance,
                        field,
                        compress_image(
                            self.cleaned_data[f"{field}"],
                            is_medium_thumbnail=self.fields.get(
                                f"{field}"
                            ).is_medium_thumbnail,
                            is_small_thumbnail=self.fields.get(
                                f"{field}"
                            ).is_small_thumbnail,
                            is_big_thumbnail=self.fields.get(
                                f"{field}"
                            ).is_big_thumbnail,
                            is_extra_small=self.fields.get(f"{field}").is_extra_small,
                            quality=getattr(self.fields.get(f"{field}"), "quality"),
                        ),
                    )
            instance.save()
            return instance


class GeneralCompressImageForm(BaseModelForm):
    image = ImageField(label="Картинка", is_medium_thumbnail=True, quality=80)