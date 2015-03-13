import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GladiatorTeamProject.settings')

import django
django.setup()

from Spartacus.models import Item, Avatar,AvatarItem

def populate():
    add_item(name= "Sword of destruction",
        price = "100",
        itemType = "sword",
        attack = "42",
        deffence = "62",
        picture = "item_images/sword1.jpg")

    add_item(name= "Magic sword",
        price = "250",
        itemType = "sword",
        attack = "120",
        deffence = "70",
        picture = "item_images/sword2.jpg")

    add_item(name= "Sword of death",
        price = "90",
        itemType = "sword",
        attack = "50",
        deffence = "40",
        picture = "item_images/sword3.jpg")

    add_item(name= "Shield of horror",
        price = "130",
        itemType = "shield",
        attack = "80",
        deffence = "100",
        picture = "item_images/shield1.jpg")

    add_item(name= "Dragon shield",
        price = "150",
        itemType = "shield",
        attack = "70",
        deffence = "120",
        picture = "item_images/shield2.jpg")

    add_item(name= "Shield of poison",
        price = "60",
        itemType = "shield",
        attack = "30",
        deffence = "65",
        picture = "item_images/shield3.jpg")

    add_item(name= "Leather armor",
        price = "50",
        itemType = "armor",
        attack = "20",
        deffence = "45",
        picture = "item_images/armor1.jpg")

    add_item(name= "Copper armor",
        price = "140",
        itemType = "armor",
        attack = "60",
        deffence = "120",
        picture = "item_images/armor2.jpg")

    add_item(name= "Iron armor",
        price = "180",
        itemType = "armor",
        attack = "70",
        deffence = "100",
        picture = "item_images/armor3.jpg")


def add_item(name, price, itemType, attack, deffence, picture):
    i = Item.objects.get_or_create(name = name,
                                   price = price,
                                   itemType = itemType,
                                   attack = attack,
                                   deffence = deffence,
                                   picture =  picture)[0]
    return i

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()