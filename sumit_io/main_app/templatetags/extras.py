from django import template
from django.template.defaultfilters import stringfilter
register=template.Library()

@register.filter
@stringfilter
def concat(value1,value2="assets/img/",inverse=True):
        if inverse:return value2+value1
        else:return value1+value2