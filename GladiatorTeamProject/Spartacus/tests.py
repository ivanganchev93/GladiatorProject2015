from django.test import TestCase
from django.contrib.auth.models import User
from Spartacus.models import Avatar, AvatarItem, Item
from Spartacus.fight_func import fight
from Spartacus.views import getItems
from django.core.urlresolvers import reverse

def add_user(username, password):
    user = User.objects.create_user(username=username, password = password)
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
        
    #def test_only_one_avatar_item_type_equiped(self):
        ''' 
        Testing that a user can only have one item of a particular type equipped
        '''
        #item1 = add_item('sword', 50, 'sowrdA', 20, 10) 
        #item2 = add_item('sword', 50, 'sowrdB', 20, 10)
        #avatar_item1 = add_avatar_item(self.avatar, item1, True)
        #avatar_item2 = add_avatar_item(self.avatar, item2, True)
        #self.assertFalse(avatar_item1.equiped)
        
    def test_correct_itemType_assignment(self):
        item1 = add_item('boots', 100, 'SomeBoots', 10, 20)
        avatar_item1 = add_avatar_item(self.avatar, item1, True)
        self.assertEquals(avatar_item1.item.itemType, 'boots')
        
class FightFunctionTest(TestCase):

    def setUp(self):
        self.user1 = add_user('Maximus', 'Max')
        self.avatar1 = add_avatar(self.user1)
        self.user2 = add_user('Minimus', 'Min')
        self.avatar2 = add_avatar(self.user2)
        
    def  test_player_stat_update(self):
        '''
        testing that the fight function behaves correctly
        '''
        for i in range(20): #creating 20 fights to tests multiple results
            initial_strength = self.avatar1.strength
            initial_agility = self.avatar1.agility
            initial_intelligence = self.avatar1.intelligence
            initial_deffence = self.avatar1.deffence
            initial_attack = self.avatar1.attack
        
            fightData = fight(self.avatar1, self.avatar2)
            if fightData['result'] == 1:
                self.assertEquals(initial_strength+2, self.avatar1.strength)
                self.assertEquals(initial_agility+2, self.avatar1.agility)
                self.assertEquals(initial_intelligence+1, self.avatar1.intelligence)
                self.assertEquals(initial_deffence+2, self.avatar1.deffence)
                self.assertEquals(initial_attack+2, self.avatar1.attack)
            
            elif fightData['result'] == 0:
                self.assertEquals(initial_strength+1, self.avatar1.strength)
                self.assertEquals(initial_agility+1, self.avatar1.agility)
                self.assertEquals(initial_intelligence, self.avatar1.intelligence)
                self.assertEquals(initial_deffence+1, self.avatar1.deffence)
                self.assertEquals(initial_attack+1, self.avatar1.attack)
            
            else:
                self.assertEquals(initial_deffence+1, self.avatar1.deffence)
                self.assertEquals(initial_attack+1, self.avatar1.attack)
                
class GetItemsTest(TestCase):

    def setUp(self):
        self.user = add_user('Maximus', 'Max')
        self.avatar = add_avatar(self.user) 
        
    def test_getItems_function(self):
        item1 = add_item('sword', 50, 'sowrdA', 20, 10) 
        item2 = add_item('shield', 50, 'shieldB', 20, 10)
        item3 = add_item('boots', 50, 'bootsC', 20, 10)
        item4 = add_item('armor', 50, 'armoeD', 20, 10)
        avatar_item1 = add_avatar_item(self.avatar, item1, True)
        avatar_item2 = add_avatar_item(self.avatar, item2, True)
        avatar_item3 = add_avatar_item(self.avatar, item3, False)
        avatar_item4 = add_avatar_item(self.avatar, item4, False)
        dict =  getItems(self.avatar)
        self.assertTrue(avatar_item1 in dict['equiped_items'] and avatar_item2 in dict['equiped_items'])
        self.assertTrue(avatar_item3 in dict['inventory_items'] and avatar_item4 in dict['inventory_items'])
        
class ViewTest(TestCase):
    
    def setUp(self):
        self.user = add_user('Maximus', 'Max')
        self.avatar = add_avatar(self.user)
        self.user2 = add_user('Minimus', 'Min')
        self.avatar2 = add_avatar(self.user2)
        self.client.login(username='Maximus', password='Max')
        
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Spartacus')
    
    def test_avatar_view(self):
        response = self.client.get('/Spartacus/avatar_view/' + self.user.username)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.avatar.attack)
        self.assertContains(response, self.avatar.deffence)
        
    def test_leaderboard_view(self):
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertTrue(self.avatar in response.context['avatars'])
        
    def test_arena_view(self):
        response = self.client.get(reverse('arena'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user2.username)
        
    def test_questing_view(self):
        response = self.client.get(reverse('questing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Body Parts")
        self.assertContains(response, "The Mercenaries")
        self.assertContains(response, "Precision")
        self.assertContains(response, "Philosophy")
        
    def test_market_view(self):
        item1 = add_item('sword', 50, 'sowrdA', 20, 10) 
        item2 = add_item('shield', 50, 'shieldB', 20, 10)
        response = self.client.get(reverse('market'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, item1.name)
        self.assertContains(response, item1.price)
        self.assertContains(response, item2.name)
        self.assertContains(response, item2.price)