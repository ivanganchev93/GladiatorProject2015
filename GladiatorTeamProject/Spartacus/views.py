from django.shortcuts import render
from Spartacus.forms import AvatarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Spartacus.models import User, Avatar, AvatarItem, Item
from random import randint
from datetime import datetime
from Spartacus.fight_func import fight


def getItems(avatar):
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
        context_dict['avatar'] = avatar
    except:
        print "Query fail getItems function"
    return context_dict



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
    
    #Allowed to fight variables here
    timePassed = True

    fightStartedAt = request.session.get("fightStartedAt")

    if fightStartedAt and fightStartedAt!=0:
        fightStartedAtTime = datetime.strptime(fightStartedAt[:-7], "%Y-%m-%d %H:%M:%S")
        time_elapsed = (datetime.now() - fightStartedAtTime).seconds
        waitTime = 10
        if time_elapsed < waitTime:
            timePassed = False
        else:
            request.session['fightStartedAt']=0
        context_dict['time_left'] = waitTime - time_elapsed
    context_dict['time_passed'] = timePassed
    
    try:
        user = User.objects.get(username = name)
        avatar = Avatar.objects.get(user = user)
        health = avatar.strength*25;
        
        context_dict.update(getItems(avatar))
        
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
            # avatar cannot have more than 8 items in inventory
            inventory_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = False)
            item_name = request.POST['item']
            item = Item.objects.get(name = item_name)
            if item.price <= avatar.cash:
                if(len(inventory_items) < 8):
                    #create an AvatarItem instance if the avatar has enough money
                    avatarItem = AvatarItem.objects.create(item = item, avatar = avatar)
                    avatar.cash = avatar.cash - item.price
                    avatar.save()
                    context_dict["bought"] = item.name
                else: context_dict["bought"] = "full inventory"


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
     
    context_dict = getItems(avatar)
    
    return render(request, 'Spartacus/item_list.html', context_dict)



@login_required
def unequip_item(request):
    item_id = None
    context_dict = {}

    if request.method == 'GET':
        item_id = request.GET['item_id']

    if item_id:
        item = AvatarItem.objects.get(id = item_id)
        avatar = item.avatar
        inventory_items = AvatarItem.objects.filter(avatar = avatar).filter(equiped = False)
        if(len(inventory_items) < 8):
            if item:
                item.equiped = False
                item.save()
        else:
            context_dict["full"] = True

    context_dict.update(getItems(avatar))
    
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
    
@login_required
def sell_item(request):
    item_id = None
    if request.method == 'GET':
        item_id = request.GET['item_id']
        
    if item_id:
        item = AvatarItem.objects.get(id = item_id)
        avatar = item.avatar
    sell_amount = int(item.item.price * 0.3) #sell an item at 30% of original price
    avatar.cash += sell_amount
    item.delete()
    avatar.save()
    
    context_dict = getItems(avatar)
    
    return render(request, 'Spartacus/item_list.html', context_dict)
    