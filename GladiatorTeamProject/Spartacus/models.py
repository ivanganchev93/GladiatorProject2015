from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Avatar(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    cash = models.IntegerField(default = 100)
    attack = models.IntegerField(default= 10)
    deffence = models.IntegerField(default= 10)

    strength = models.IntegerField(default= 10)
    agility = models.IntegerField(default= 10)
    intelligence = models.IntegerField(default = 10)

    # Fight fields
    #isFighting = models.BooleanField(default=False)
    #fightStartedAt = models.DateField(default=datetime.now())
    victories = models.IntegerField(default = 0)
    points = models.IntegerField(default = 0) # for ranking...every time a gladiator fights get some amount of points
    # that determines his position in the rankings

    def __unicode__(self):
        return self.user.username

class Item(models.Model):   
    ITEM_CHOICES = (
    ('sword', 'sword'),
    ('shield', 'shield'),
    ('armor', 'armor'),
    ('helmet', 'helmet'),
    ('boots', 'boots'),)

    price = models.IntegerField(default = 0)
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

    # override the save method to ensure only one item per type can be equiped
    def save(self, *args, **kwargs):
        items = Item.objects.filter(itemType = self.item.itemType)

        if self.equiped:
            for item in items:
                AvatarItem.objects.filter(item = item, avatar = self.avatar,
                    equiped=True).update(equiped=False)
        super(AvatarItem, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.item.name





