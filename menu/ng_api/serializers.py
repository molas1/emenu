from rest_framework import serializers

from menu.models import Menu, Dish


class MenuSerializer(serializers.ModelSerializer):
    dish_count = serializers.SerializerMethodField()

    def get_dish_count(self, obj):
        return obj.dish_count

    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'created', 'modified', 'dish_count')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'created', 'modified', 'price', 'preparation_time', 'vegan', 'image')

    def to_representation(self, instance):
        serialized = super().to_representation(instance)
        if instance.image:
            image_url = instance.image.url
            serialized['image'] = image_url
        return serialized
