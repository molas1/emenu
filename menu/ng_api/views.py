from django.db.models import Count
from rest_framework import generics, filters

from menu.models import Menu, Dish
from menu.ng_api.serializers import MenuSerializer, DishSerializer
from menu.ng_api.pagination import DefaultPagination


class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.annotate(dish_count=Count('dishes')).exclude(dish_count=0)
    serializer_class = MenuSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pk', 'name', 'dish_count')
    pagination_class = DefaultPagination


class MenuDishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']
        if menu_id is not None:
            return self.queryset.filter(menu__id=menu_id)
        return self.queryset
