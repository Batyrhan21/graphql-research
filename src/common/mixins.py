from django.utils.html import format_html


class ImageTagMixin:
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img style="width: 200px; height: 200px;" src="{}" />'.format(
                    obj.image.url
                )
            )

    image_tag.short_description = "Превью"


class ShortTextMixin:
    def short_description(self, obj):
        if obj.description:
            return format_html(
                '<p>{}</p>'.format(
                    obj.description[0:100]
                )
            )