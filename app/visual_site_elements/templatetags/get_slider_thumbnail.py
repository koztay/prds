from django import template
from ..models import SliderImage, SLIDER_THUMB_CHOICES

register = template.Library()


@register.filter
def get_slider_thumbnail(obj, arg):
    """
    obj == Product instance

    """
    arg = arg.lower()
    if not isinstance(obj, SliderImage):
        raise TypeError("This is not a valid product model.")
    choices = dict(SLIDER_THUMB_CHOICES)
    if not choices.get(arg):
        raise TypeError("This is not a valid type for this model.")
    try:
        return obj.sliderthumbnail_set.filter(type=arg).first().media.url
    except:
        return None
