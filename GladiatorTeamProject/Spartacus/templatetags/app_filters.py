from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='mulLeft')
def mulLeft(value,value2):
    return (value%4)*value2

@register.filter(name='mulTop')
def mulTop(value,value2):
    if value < 4:
        return 1*value2
    else:
        return 100+value2