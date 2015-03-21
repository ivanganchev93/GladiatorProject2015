import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GladiatorTeamProject.settings')

import django
django.setup()

from Spartacus.models import User, Avatar, AvatarItem, Item

def populate():
    user1  = add_user("Leonid", "leonid@gmail.com", "12345")
    user2 = add_user("Claudius", "claudius@gmail.com", "12345")
    user3 = add_user("Tiberius", "tiberius@gmail.com", "12345")
    user4 = add_user("Trajan", "trajan@gmail.com", "12345")
    user5 = add_user("Augustus", "augustus@gmail.com", "12345")

    avatar1 = add_avatar(user1, 30, 30, 20, 15 ,10, "profile_images/leonid.jpg")
    avatar2 = add_avatar(user2, 40, 50, 20, 30 ,20, "profile_images/claudius.jpg")
    avatar3 = add_avatar(user3, 30, 30, 50, 45 ,20, "profile_images/tiberius.jpg")
    avatar4 = add_avatar(user4, 10, 15, 20, 15 ,10, "profile_images/trajan.jpg")
    avatar5 = add_avatar(user5, 50, 40, 30, 35 ,20, "profile_images/augustus.jpg")

    sword1 = add_item(name= "Sword of destruction",
        price = "100",
        itemType = "sword",
        attack = "42",
        deffence = "62",
        picture = "item_images/sword1.jpg")

    sword2 = add_item(name= "Magic sword",
        price = "250",
        itemType = "sword",
        attack = "120",
        deffence = "70",
        picture = "item_images/sword2.jpg")

    sword3 = add_item(name= "Sword of death",
        price = "90",
        itemType = "sword",
        attack = "50",
        deffence = "40",
        picture = "item_images/sword3.jpg")

    shield1 = add_item(name= "Shield of horror",
        price = "130",
        itemType = "shield",
        attack = "80",
        deffence = "100",
        picture = "item_images/shield1.jpg")

    shield2 = add_item(name= "Dragon shield",
        price = "150",
        itemType = "shield",
        attack = "70",
        deffence = "120",
        picture = "item_images/shield2.jpg")

    shield3 = add_item(name= "Shield of poison",
        price = "60",
        itemType = "shield",
        attack = "30",
        deffence = "65",
        picture = "item_images/shield3.jpg")

    armor1 = add_item(name= "Leather armor",
        price = "50",
        itemType = "armor",
        attack = "20",
        deffence = "45",
        picture = "item_images/armor1.jpg")

    armor2 = add_item(name= "Copper armor",
        price = "140",
        itemType = "armor",
        attack = "60",
        deffence = "120",
        picture = "item_images/armor2.jpg")

    armor3 = add_item(name= "Iron armor",
        price = "180",
        itemType = "armor",
        attack = "70",
        deffence = "100",
        picture = "item_images/armor3.jpg")

    helmet1 = add_item(name= "Iron helmet",
        price = "90",
        itemType = "helmet",
        attack = "50",
        deffence = "60",
        picture = "item_images/helmet1.jpg")

    helmet2 = add_item(name= "Centurio helmet",
        price = "250",
        itemType = "helmet",
        attack = "100",
        deffence = "190",
        picture = "item_images/helmet2.jpg")

    helmet3 = add_item(name= "Copper helmet",
        price = "140",
        itemType = "helmet",
        attack = "80",
        deffence = "100",
        picture = "item_images/helmet3.jpg")

    boots1 = add_item(name= "Sandals",
        price = "80",
        itemType = "boots",
        attack = "60",
        deffence = "50",
        picture = "item_images/boots1.jpg")

    boots2 = add_item(name= "Golden boots",
        price = "180",
        itemType = "boots",
        attack = "100",
        deffence = "110",
        picture = "item_images/boots2.jpg")

    boots3 = add_item(name= "Leather warrior sandals ",
        price = "140",
        itemType = "boots",
        attack = "80",
        deffence = "100",
        picture = "item_images/boots3.jpg")

    add_avatar_item(sword1, avatar1, True)
    add_avatar_item(helmet2, avatar1, False)
    add_avatar_item(armor3, avatar1, True)
    add_avatar_item(shield1, avatar1, False)
    add_avatar_item(boots2, avatar1, True)

    add_avatar_item(sword2,avatar2, True)
    add_avatar_item(helmet3,avatar2, False)
    add_avatar_item(shield2,avatar2, False)
    add_avatar_item(boots1,avatar2, True)
    add_avatar_item(boots2,avatar2, False)
    add_avatar_item(armor1,avatar2, True)

    add_avatar_item(sword1,avatar3, True)
    add_avatar_item(boots3,avatar3, True)
    add_avatar_item(shield2,avatar3, False)
    add_avatar_item(armor1,avatar2, False)

    add_avatar_item(sword3,avatar4, True)
    add_avatar_item(shield3,avatar4, True)

    add_avatar_item(boots1,avatar5, True)
    add_avatar_item(armor2,avatar5, True)
    add_avatar_item(sword1,avatar5, True)
    add_avatar_item(armor3,avatar5, False)
    add_avatar_item(shield3,avatar5, False)


def add_avatar_item(item, avatar, equiped):
    avatar_item = AvatarItem.objects.get_or_create(item = item, avatar = avatar, equiped = equiped)[0]
    return avatar_item

def add_item(name, price, itemType, attack, deffence, picture):
    i = Item.objects.get_or_create(name = name,
                                   price = price,
                                   itemType = itemType,
                                   attack = attack,
                                   deffence = deffence,
                                   picture =  picture)[0]
    return i

def add_user(username, email, password):
    user = User.objects.get_or_create(username=username,
                                      email=email)[0]
    user.set_password(password)
    user.save()
    return user


def add_avatar(user, attack, deffence, strength, agility, intelligence, picture):
    avatar = Avatar.objects.get_or_create(user = user,
                                          attack = attack,
                                          deffence = deffence,
                                          strength = strength,
                                          agility = agility,
                                          intelligence = intelligence,
                                          picture = picture)[0]
    return avatar

# Start execution here!
if __name__ == '__main__':
    print "Starting Spartacus population script..."
    populate()