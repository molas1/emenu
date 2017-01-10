import pytest
import mock

from menu.ng_api.serializers import DishSerializer
from menu.ng_api.views import MenuDishListView
from menu.models import Dish


FAKE_IMAGE_URL = '/static/fake_dish.png'


def get_fake_dish_model(fake_image_url):
    dish_model = Dish()

    fake_image = None
    if fake_image_url:
        fake_image = mock.Mock()
        fake_image.url = fake_image_url

    dish_model.image = fake_image
    return dish_model


class TestDishSerializer:
    @pytest.mark.parametrize('fake_image_url', (None, FAKE_IMAGE_URL))
    def test_to_representation_retrieves_image_url_property(self, fake_image_url):
        dish_serializer = DishSerializer()
        fake_dish_model = get_fake_dish_model(fake_image_url=fake_image_url)
        assert fake_image_url == dish_serializer.to_representation(instance=fake_dish_model)['image']


class TestMenuDishListView:
    def test_get_queryset_returns_dishes_filtered_by_menu(self):
        v = MenuDishListView()
        menu_id = 3
        v.kwargs = {'menu_id': menu_id}
        fake_queryset = mock.Mock()
        v.queryset = fake_queryset
        filtered_queryset = v.get_queryset()

        assert filtered_queryset
        fake_queryset.filter.assert_called_once_with(menu__id=menu_id)
