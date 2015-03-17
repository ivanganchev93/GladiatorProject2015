from django.shortcuts import render
from Spartacus.forms import AvatarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Spartacus.models import User, Avatar, AvatarItem, Item
from random import randint

def fight(you, opponent):
    try:
        # items that are equiped
        yourItems = AvatarItem.objects.filter(avatar = you, equiped = True)
        opponentItems = AvatarItem.objects.filter(avatar = opponent, equiped = True)


        youAttack = you.attack
        youDeffence = you.deffence
        opponentAttack = opponent.attack
        opponentDeffence = opponent.deffence

        # update attack and defence
        for item in yourItems:
            youAttack += item.item.attack
            youDeffence += item.item.deffence
        for item in opponentItems:
            opponentAttack += item.item.attack
            opponentDeffence += item.item.deffence

        # both gladiators start the fight with 100 health
        youHealth = 100
        opponentHealth = 100

        # the hit chance depends on the intelligence
        hitRatio = (you.intelligence + opponent.intelligence) * 1.0
        youHitChance = (you.intelligence / hitRatio) * 100 # in percentages
        opponentHitChance = (opponent.intelligence / hitRatio) * 100  # in percentages

        # chance of double hit depends on the agility and the initial hit chance
        doubleHitRatio = (you.agility + opponent.agility) * 1.0
        youDoubleHitChance = (youHitChance * (you.agility / doubleHitRatio))
        opponentDoubleHitChance = (opponentHitChance * (opponent.agility / doubleHitRatio))


        # damage
        youDamage = (youAttack + opponentDeffence) / opponentDeffence
        opponentDamage = (opponentAttack + youDeffence) / youDeffence

        while youHealth > 0 and opponentHealth > 0:
            if randint(0,100) <= int(youHitChance):
                opponentHealth -= youDamage
            if randint(0,100) <= int(youDoubleHitChance):
                opponentHealth -= youDamage * 2

            if randint(0,100) <= int(opponentHitChance):
                youHealth -= opponentDamage
            if randint(0,100) <= int(opponentDoubleHitChance):
                youHealth -= opponentDamage * 2

        #victory
        if youHealth > opponentHealth:
            you.points += 50
            you.victories += 1

            cashWon = opponent.cash / 10.0  # 10% of the opponent's cash
            you.cash += cashWon
            opponent.cash -= cashWon
            
            #updating stats
            you.attack += 2
            you.deffence += 2
            you.strength += 2
            you.agility += 2
            you.intelligence += 1

            you.save()
            opponent.save()
            return 1

        #defeat
        elif youHealth < opponentHealth:
            #updating stats
            you.attack += 1
            you.deffence += 1
            you.points += 20
            you.save()
            return -1
        
        #tie
        else:
            #updating stats
            you.attack += 1
            you.deffence += 1
            you.strength += 1
            you.agility += 1
            you.points += 30
            you.save()
            return 0
    except:
        print "Query fail battle"


def index(request):
    context_dict = {'message': "SPARTACUS"}
    return render(request, 'Spartacus/index.html', context_dict)


def add_profile(request):
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        profile_form = AvatarForm(data = request.POST)

        # If the two forms are valid...
        if profile_form.is_valid():
            f = profile_form.save(commit = False)
            f.user_id = request.user.id
            profile_form.save()

            if 'picture' in request.FILES:
                f.picture = request.FILES['picture']
            f.save()

            return HttpResponseRedirect('/Spartacus/')
        else:
            print profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        profile_form = AvatarForm()

    # Render the template depending on the context.
    return render(request, 'Spartacus/add_profile.html',   {'profile_form': profile_form} )

def avatar_view(request, name):
    context_dict = {}
    try:
        user = User.objects.get(username = name)
        avatar = Avatar.objects.get(user = user)
        health = avatar.strength*100;
        inventory_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = False)
        equiped_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = True)
        context_dict['avatar'] = avatar
        context_dict['equiped_items'] = equiped_items
        context_dict['inventory_items'] = inventory_items
        context_dict['health']= health
    except:
        print "Query fail Avatar_view"
    return render(request, 'Spartacus/avatar_view.html', context_dict)

@login_required    
def arena(request):
    context_dict = {}
    user = request.user
    try:
        opponents = Avatar.objects.exclude(user = user).order_by('-points')
        you = Avatar.objects.get(user = user)
        #your relevant opponents are the one with similar points to you
        relevant_opponents = []
        for opponent in opponents:
            point_difference = int(opponent.points) - int(you.points)
            if point_difference < 200 and point_difference > - 200:
                relevant_opponents += [opponent]
        context_dict['opponents'] = relevant_opponents
    except:
        print "Query fail Arena"
    return render(request, 'Spartacus/arena.html', context_dict)
    
@login_required
def battle(request, opponent):
    context_dict = {}
    try:
        you = Avatar.objects.get(user = request.user)
        opposing_user = User.objects.get(username = opponent)
        opponent = Avatar.objects.get(user = opposing_user)
        victory = fight(you, opponent)
        context_dict['you'] = you
        context_dict['opponent'] = opponent
        context_dict['victory'] = victory
    except:
        print "Query fail battle"
        return HttpResponseRedirect('/Spartacus/arena')
    return render(request, 'Spartacus/battle.html', context_dict)
    
@login_required
def market(request):
    context_dict = {}
    try:
        avatar = Avatar.objects.get(user = request.user)
        items = Item.objects.order_by('-price')
        context_dict['items'] = items
        
        if request.method == 'POST':
            item_name = request.POST['item']
            item = Item.objects.get(name = item_name)
            if item.price <= avatar.cash:
                #create an AvatarItem instance if the avatar has enough money
                avatarItem = AvatarItem.objects.create(item = item, avatar = avatar)
                avatar.cash = avatar.cash - item.price
                avatar.save()
                context_dict["bought"] = item.name
            else:
                context_dict["bought"] = "Insufficient cash"
    except:
        print "Query fail market"
    return render (request, 'Spartacus/market.html', context_dict)
    
def leaderboard(request):
    context_dict = {}
    try:
        #list of top 20
        avatars = Avatar.objects.order_by('-points')[:20]
        context_dict['avatars'] = avatars
    except:
        print "Query fail leaderboard"
    return render(request, 'Spartacus/leaderboard.html', context_dict)


@login_required
def equip_item(request):
    item_id = None
    if request.method == 'GET':
        item_id = request.GET['item_id']
    
    if item_id:
        item = AvatarItem.objects.get(id = item_id)
        avatar = item.avatar
        if item:
            item.equiped = True
            item.save()
    
    context_dict = {}
    
    try:
        inventory_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = False)
        equiped_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = True)

        context_dict['equiped_items'] = equiped_items
        context_dict['inventory_items'] = inventory_items
    except:
        print "Query fail equip_item"
    return render(request, 'Spartacus/item_list.html', context_dict)



@login_required
def unequip_item(request):
    item_id = None
    if request.method == 'GET':
        item_id = request.GET['item_id']

    if item_id:
        item = AvatarItem.objects.get(id = item_id)
        avatar = item.avatar
        if item:
            item.equiped = False
            item.save()

    context_dict = {}

    try:
        inventory_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = False)
        equiped_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = True)

        context_dict['equiped_items'] = equiped_items
        context_dict['inventory_items'] = inventory_items
    except:
        print "Query fail equip_item"
    return render(request, 'Spartacus/item_list.html', context_dict)
