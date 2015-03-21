from django.test import TestCase
from django.contrib.auth.models import User
from Spartacus.models import Avatar, AvatarItem, Item

def add_user(username, password):
    user = User.objects.get_or_create(username=username, password = password)[0]
    return user
    
def add_avatar(user):
    avatar = Avatar.objects.get_or_create(user = user)[0]
    return avatar
    
def add_item(itemType, price, name, attack, defence):
    picture =  'item_images/sword2.jpg'
    item = Item.objects.get_or_create(name = name, picture = picture)[0]
    item.itemType = itemType
    item.price = price
    item.attack = attack
    item.defence = defence
    item.save()
    return item
    
def add_avatar_item(avatar, item, equiped):
     avatar_item = AvatarItem.objects.get_or_create(avatar = avatar, item = item)[0]
     avatar_item.equiped = equiped
     avatar_item.save()
     return avatar_item
     
class AvatarItemTests(TestCase):

    def setUp(self):
        self.user = add_user('Maximus', 'Max')
        self.avatar = add_avatar(self.user)

    def test_multiple_items_can_be_equiped(self):
        ''' 
        Testing that a user can equip multiple items
        '''
        item1 = add_item('sword', 50, 'sowrdA', 20, 10) 
        item2 = add_item('shield', 50, 'shieldB', 20, 10)
        avatar_item1 = add_avatar_item(self.avatar, item1, True)
        avatar_item2 = add_avatar_item(self.avatar, item2, True)
        self.assertTrue(avatar_item1.equiped)
        self.assertTrue(avatar_item2.equiped)
        
    def test_only_one_avatar_item_type_equiped(self):
        ''' 
        Testing that a user can only have one item of a particular type equipped
        '''
        item1 = add_item('sword', 50, 'sowrdA', 20, 10) 
        item2 = add_item('sword', 50, 'sowrdB', 20, 10)
        avatar_item1 = add_avatar_item(self.avatar, item1, True)
        avatar_item2 = add_avatar_item(self.avatar, item2, True)
        self.assertFalse(avatar_item1.equiped)