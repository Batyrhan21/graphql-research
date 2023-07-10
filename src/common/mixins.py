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


class PhotoTagAdminMixin:
    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<div style="width: 80px; height: 80px; '
                'border-radius: 50%; overflow: hidden; '
                'margin-right: 10px;">'
                '<img src="{}" style="width: 100%; height: 100%; '
                'object-fit: cover;" />'
                '</div>'.format(obj.photo.url)
            )
        else:
            return format_html(
                '<div style="width: 80px; height: 80px; '
                'border-radius: 50%; background-color: #eee; '
                'display: flex; justify-content: center; align-items: center; '
                'font-size: 24px; color: #aaa; margin-right: 10px; '
                'text-align: center;">'
                'Пусто'
                '</div>'
            )