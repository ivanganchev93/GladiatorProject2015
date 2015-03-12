from django import forms
from django.contrib.auth.models import User
from Spartacus.models import Avatar, AvatarItem, Item

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('picture',)

