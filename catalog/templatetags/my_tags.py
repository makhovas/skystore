from django import template

from skystore import settings

register = template.Library()


@register.simple_tag
def mediafile(image):
    return f'/media/{image}'


@register.filter
def mediafile_filter(image):
    media_root = settings.MEDIA_URL
    return f'{media_root}{image}'
