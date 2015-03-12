import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GladiatorTeamProject.settings')

import django
django.setup()

from Spartacus.models import Item, Avatar,AvatarItem

def populate():
    add_item(name= "Sword of destruction",
        itemType = "sword",
        attack = "42",
        deffence = "62",
        picture = "item_images/sword1.jpg")

    add_item(name= "Magic sword",
        itemType = "sword",
        attack = "120",
        deffence = "70",
        picture = "item_images/sword2.jpg")

    add_item(name= "Sword of death",
        itemType = "sword",
        attack = "50",
        deffence = "40",
        picture = "item_images/sword3.jpg")

    add_item(name= "Shield of horror",
        itemType = "shield",
        attack = "80",
        deffence = "100",
        picture = "item_images/shield1.jpg")

    add_item(name= "Dragon shield",
        itemType = "shield",
        attack = "70",
        deffence = "120",
        picture = "item_images/shield2.jpg")

    add_item(name= "Shield of poison",
        itemType = "shield",
        attack = "30",
        deffence = "65",
        picture = "item_images/shield3.jpg")

    add_item(name= "Leather armor",
        itemType = "armor",
        attack = "20",
        deffence = "45",
        picture = "item_images/armor1.jpg")

    add_item(name= "Copper armor",
        itemType = "armor",
        attack = "60",
        deffence = "120",
        picture = "item_images/armor2.jpg")

    add_item(name= "Iron armor",
        itemType = "armor",
        attack = "70",
        deffence = "100",
        picture = "item_images/armor3.jpg")


def add_item(name, itemType, attack, deffence, picture):
    i = Item.objects.get_or_create(name = name,
                                   itemType = itemType,
                                   attack = attack,
                                   deffence = deffence,
                                   picture =  picture)[0]
    return i

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()