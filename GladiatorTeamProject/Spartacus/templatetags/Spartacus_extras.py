from django import template
from Spartacus.models import User, Avatar, AvatarItem, Item
from Spartacus.views import getItems

register = template.Library()

@register.inclusion_tag('Spartacus/item_list.html', takes_context=True)
def get_items(avatar, context):
    request = context['request']
    return getItems(avatar)