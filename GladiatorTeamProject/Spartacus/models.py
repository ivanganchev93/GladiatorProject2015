from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    attack = models.IntegerField(default= 10)
    deffence = models.IntegerField(default= 10)

    strength = models.IntegerField(default= 10)
    agility = models.IntegerField(default= 10)

    def __unicode__(self):
        return self.user.username

class Item(models.Model):   
    ITEM_CHOICES = (
    ('sword', 'sword'),
    ('shield', 'shield'),
    ('armor', 'armor'),)
    
    itemType = models.CharField(max_length=128, choices=ITEM_CHOICES, default= 'sword')
    
    name = models.CharField(max_length=128, unique = True)
    picture = models.ImageField(upload_to='item_images', blank=True)
    
    attack = models.IntegerField(default= 10)
    deffence = models.IntegerField(default= 10)
   
    def __unicode__(self):
        return self.name

class AvatarItem(models.Model):
    item = models.ForeignKey(Item)
    avatar = models.ForeignKey(Avatar)
    
    equiped = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.item.name





