from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '<%s> id: %s, name: %s' % (self.__class__.__name__, self.id, self.name)


class Menu(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField()


class Dish(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    preparation_time = models.TimeField(null=False)
    vegan = models.BooleanField(default=False)
    image = models.ImageField(upload_to='', null=True, blank=True)

    menu = models.ForeignKey('Menu', related_name='dishes')

    class Meta:
        verbose_name_plural = 'Dishes'
