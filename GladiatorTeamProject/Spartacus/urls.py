from django.conf.urls import patterns, url
from Spartacus import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_profile/$', views.add_profile, name='add_profile'),
        url(r'^avatar_view/(?P<name>[\w\-]+)$', views.avatar_view, name='avatar_view'),
        url(r'^arena/$', views.arena, name='arena'),
        url(r'^battle/(?P<opponent>[\w\-]+)$', views.battle, name='battle'),
        url(r'^market/$', views.market, name='market'),
        url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
        url(r'^equip_item/$', views.equip_item, name='equip_item'),
        url(r'^unequip_item/$', views.unequip_item, name='unequip_item'),
        url(r'^unequip_item_market/$', views.unequip_item_market, name='unequip_item_market'),
        url(r'^questing/$', views.questing, name='questing'),
        url(r'^sell_item/$', views.sell_item, name='sell_item'))
