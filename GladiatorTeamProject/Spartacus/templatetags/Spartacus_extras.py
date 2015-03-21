from django import template
from Spartacus.models import User, Avatar, AvatarItem, Item
from Spartacus.views import getItems

register = template.Library()

@register.inclusion_tag('Spartacus/item_list.html', takes_context=True)
def get_items(context):
    avatar = context['avatar']
    user = context['user']
    context_dict = getItems(avatar)
    context_dict['user'] = user
    context_dict['time_passed'] = context["time_passed"]
    return context_dict

@register.inclusion_tag('Spartacus/item_list_market.html',takes_context=True)
def get_market_items(context):
    avatar = context['avatar']
    context_dict = getItems(avatar)
    context_dict['bought'] = context['bought']
    return context_dict