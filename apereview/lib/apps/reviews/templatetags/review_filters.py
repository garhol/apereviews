from django import template

register = template.Library()
    
@register.filter
def apescore(value):
    divided = float(int(value)*0.5)
    return "%s/5" % divided
