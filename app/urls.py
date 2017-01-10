from django.conf.urls import url
from django.contrib import admin

from menu.views import IndexView
from menu.ng_api.views import MenuListAPIView, MenuDishListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='index'),

    # menu-views
    url(r'^ng-api/menu/$', MenuListAPIView.as_view(), name='ng-api-menu-list'),
    url(r'^ng-api/menu/(?P<menu_id>\d+)/$', MenuDishListView.as_view(), name='ng-api-menu-detail')
]
