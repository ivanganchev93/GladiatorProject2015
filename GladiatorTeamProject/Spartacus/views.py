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
        print "Failed to retrieve avatar or his items"
    return render(request, 'Spartacus/avatar_view.html', context_dict)
    