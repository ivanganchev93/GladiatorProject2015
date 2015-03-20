from django.test import TestCase
from Spartacus.models import User, Avatar, AvatarItem, Item

def add_user(username, password):
    user = User.objects.get_or_create(usernae=username)[0]
    user.save()
    return user
    
def add_avatar(user):
    avatar = Avatar.objects.get_or_create(user = user)
    avatar.save()
    return avatar
    
def add_item(itemType, price, name, attack, defence):
    picture =  'item_images/sword2.jpg'
    item = Item.objects.get_or_create(name = name, picture = picture)
    item.itemType = itemType
    item.price = price
    item.attack = attack
    item.defence = defence
    item.save()
    return item