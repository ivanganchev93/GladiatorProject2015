from django.shortcuts import render
from Spartacus.forms import AvatarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Spartacus.models import Avatar, AvatarItem, Item


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

    
@login_required
def avatar_view(request):
    context_dict = {}
    try:
        avatar = Avatar.objects.get(user = request.user)
        equiped_items = AvatarItem.objects.filter(avatar = avatar)
        context_dict['avatar'] = avatar
        context_dict['equiped_items'] = equiped_items
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
    