from django.contrib import admin
from Spartacus.models import Avatar, Item, AvatarItem


class AvatarAdmin(admin.ModelAdmin):
    list_display = ['user', 'attack', 'deffence','strength', 'agility']
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'attack', 'deffence']

class AvatarItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'avatar', 'equiped']

    
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AvatarItem, AvatarItemAdmin)
