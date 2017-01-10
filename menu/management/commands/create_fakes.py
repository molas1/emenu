import decimal
import random
import subprocess

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from menu.models import Menu, Dish


class Command(BaseCommand):
    help = 'Adds fake dishes and menus'

    def _fake_name(self, fake):
        return ' '.join([fake.name(), fake.name()])

    def handle(self, *args, **options):
        # this is bad but i need the app setup to have as few steps as possible
        subprocess.call(['python', 'manage.py', 'loaddata', 'menu/fixtures/user.json'])

        fake = Faker()

        print('Creating fake data', end='', flush=True)

        for i in range(0, 500):
            menu = Menu()
            menu.name = self._fake_name(fake)
            menu.description = fake.text()

            if i % 20 == 0:
                print('.', end='', flush=True)

            menu.save()
            with transaction.atomic():
                self._create_dishes(fake=fake, menu=menu)

        print(' Done.')

    def _create_dishes(self, fake, menu):
        for _ in range(random.randint(1, 4)):
            Dish(name=self._fake_name(fake),
                 description=fake.text(),
                 price=decimal.Decimal(random.randint(1, 100) + random.random()),
                 preparation_time=fake.time_object(),
                 vegan=True if random.random() > 0.2 else False,
                 image=None,
                 menu=menu).save()
