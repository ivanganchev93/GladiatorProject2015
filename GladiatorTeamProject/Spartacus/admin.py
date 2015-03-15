from django.contrib import admin
from Spartacus.models import Avatar, Item, AvatarItem


class AvatarAdmin(admin.ModelAdmin):
    list_display = ['user', 'attack', 'deffence','strength', 'agility', 'intelligence', 'victories', 'cash', 'points']
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','itemType', 'attack', 'deffence', 'price']

class AvatarItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'avatar', 'equiped']

    
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AvatarItem, AvatarItemAdmin)
