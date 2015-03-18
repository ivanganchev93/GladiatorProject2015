from django.shortcuts import render
from Spartacus.forms import AvatarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Spartacus.models import User, Avatar, AvatarItem, Item
from random import randint
from datetime import datetime

def fight(you, opponent):
    fightData={}
    rounds=[]
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
        youHealth = you.strength*25
        opponentHealth = you.strength*25

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
        criticalYou = 0
        opponentCritical = 0
        round=1
        while youHealth > 0 and opponentHealth > 0:

            if randint(0,100) <= int(youHitChance):
                opponentHealth -= youDamage

            if randint(0,100) <= int(youDoubleHitChance):
                criticalYou = youDamage*2
                opponentHealth -= criticalYou

            if randint(0,100) <= int(opponentHitChance):
                youHealth -= opponentDamage
            if randint(0,100) <= int(opponentDoubleHitChance):
                opponentCritical = opponentDamage * 2
                youHealth -=  opponentCritical

            rounds.append({'youDamage': youDamage, 'opponentHealth': opponentHealth, 'criticalDamage': criticalYou,
                           'youHealth': youHealth, 'opponentDamage': opponentDamage,
                           'opponentCritical': opponentCritical, 'roundN': round})

            round+=1

        fightData["rounds"]=rounds
        fightData["stats"]={}

        #victory
        if youHealth > opponentHealth:
            you.points += 50
            you.victories += 1

            cashWon = opponent.cash / 10.0  # 10% of the opponent's cash
            you.cash += cashWon + 30  #30 cash extra for a victory
            opponent.cash -= cashWon
            
            #updating stats
            you.attack += 2
            you.deffence += 2
            you.strength += 2
            you.agility += 2
            you.intelligence += 1
            fightData["stats"]["attack"]=2
            fightData["stats"]["deffence"]=2
            fightData["stats"]["strength"]=2
            fightData["stats"]["agility"]=2
            fightData["stats"]["intelligence"]=2

            you.save()
            opponent.save()
            fightData['result']=1

            return fightData

        #defeat
        elif youHealth < opponentHealth:
            #updating stats
            you.attack += 1
            you.deffence += 1
            you.points += 20
            you.save()
            fightData["stats"]['result']=-1
            fightData["stats"]["attack"]=1
            fightData["stats"]["deffence"]=1
            fightData["stats"]["points"]=20
            fightData['result']=-1
            return fightData
        
        #tie
        else:
            #updating stats
            you.attack += 1
            you.deffence += 1
            you.strength += 1
            you.agility += 1
            you.points += 30
            you.save()

            fightData["stats"]["attack"]=1
            fightData["stats"]["deffence"]=1
            fightData["stats"]["strength"]=1
            fightData["stats"]["agility"]=1
            fightData["stats"]["points"]=30
            fightData['result']=0

            return fightData
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

        for equiped_item in equiped_items:
            if equiped_item.item.itemType == "helmet":
                context_dict['helmet'] = equiped_item
            elif equiped_item.item.itemType == "sword":
                context_dict['sword'] = equiped_item
            elif equiped_item.item.itemType == "armor":
                context_dict['armor'] = equiped_item
            elif equiped_item.item.itemType == "shield":
                context_dict['shield'] = equiped_item
            elif equiped_item.item.itemType == "boots":
                context_dict['boots'] = equiped_item

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
    try:
        #list of top 5
        avatars = Avatar.objects.order_by('-points')[:5]
        context_dict['avatars'] = avatars
    except:
        print "Query fail leaderboard"

    timePassed = True

    fightStartedAt = request.session.get("fightStartedAt")

    #if fight started
    if fightStartedAt and fightStartedAt!=0:
        fightStartedAtTime = datetime.strptime(fightStartedAt[:-7], "%Y-%m-%d %H:%M:%S")
        time_elapsed = (datetime.now() - fightStartedAtTime).seconds
        waitTime = 10
        if time_elapsed < waitTime:
            timePassed = False
        else:
            request.session['fightStartedAt']=0
        context_dict['time_left'] = waitTime - time_elapsed
    if timePassed:
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

    context_dict['time_passed']=timePassed

    return render(request, 'Spartacus/arena.html', context_dict)
    
@login_required
def battle(request, opponent):
    context_dict = {}

    #set start of fight
    request.session["fightStartedAt"] = str(datetime.now())

    try:
        you = Avatar.objects.get(user = request.user)
        opposing_user = User.objects.get(username = opponent)
        opponent = Avatar.objects.get(user = opposing_user)
        fightData = fight(you, opponent)

        victory = fightData['result']
        print "do not work"
        stats = fightData["stats"]

        context_dict["stats"]=stats
        context_dict['you'] = you
        context_dict['opponent'] = opponent
        context_dict['victory'] = victory
        context_dict['rounds'] = fightData['rounds']
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

        for equiped_item in equiped_items:
            if equiped_item.item.itemType == "helmet":
                context_dict['helmet'] = equiped_item
            elif equiped_item.item.itemType == "sword":
                context_dict['sword'] = equiped_item
            elif equiped_item.item.itemType == "armor":
                context_dict['armor'] = equiped_item
            elif equiped_item.item.itemType == "shield":
                context_dict['shield'] = equiped_item
            elif equiped_item.item.itemType == "boots":
                context_dict['boots'] = equiped_item

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

        for equiped_item in equiped_items:
            if equiped_item.item.itemType == "helmet":
                context_dict['helmet'] = equiped_item
            elif equiped_item.item.itemType == "sword":
                context_dict['sword'] = equiped_item
            elif equiped_item.item.itemType == "armor":
                context_dict['armor'] = equiped_item
            elif equiped_item.item.itemType == "shield":
                context_dict['shield'] = equiped_item
            elif equiped_item.item.itemType == "boots":
                context_dict['boots'] = equiped_item

        context_dict['equiped_items'] = equiped_items
        context_dict['inventory_items'] = inventory_items
    except:
        print "Query fail equip_item"
    return render(request, 'Spartacus/item_list.html', context_dict)
    
@login_required
def questing(request):
    context_dict = {}
    quest_name = None
    success = False
    time_passed = True
    #using cookies to make quest availabe once every minute
    last_played = request.session.get('last_played')
    if last_played:
        last_played_time = datetime.strptime(last_played[:-7], "%Y-%m-%d %H:%M:%S")
        time_elapsed = (datetime.now() - last_played_time).seconds
        #time before quests are available again
        wait_time = 5
        if time_elapsed < wait_time:
            time_passed = False
        context_dict['time_left'] =  wait_time - time_elapsed
    context_dict['time_passed'] = time_passed
    try:
        avatar = Avatar.objects.get(user = request.user)
        if request.method == 'POST':
            request.session['last_played'] = str(datetime.now())
            quest_name = request.POST['quest_name']
        if quest_name:
            ran = randint(0,100)
            if quest_name == "money":
                if ran > 30:
                    avatar.cash += 100
                    success = True
            elif quest_name == "workout":
                if ran > 50:
                    avatar.cash -= 50
                    avatar.strength += 2
                    success = True
            elif quest_name == "precission":
                if ran > 50:
                    avatar.cash -= 50
                    avatar.agility += 2
                    success = True
            elif quest_name == "learn":
                if ran > 60:
                    avatar.cash -= 50
                    avatar.intelligence += 1
                    success = True
            avatar.save()
            context_dict['quest_name'] = quest_name
            context_dict['success'] = success
            context_dict['questing'] = True
    except:
        print "Query fail questing"
    return render(request, 'Spartacus/questing.html', context_dict)