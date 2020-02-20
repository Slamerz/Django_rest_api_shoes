from django.core.management.base import BaseCommand
from rest_framework_shoes.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = 'Set the default Shoe colors and Types'

    @staticmethod
    def set_colors():
        colors = [
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'indigo',
            'violet',
            'white',
            'black'
        ]
        for color in colors:
            ShoeColor.objects.create(color=color)

    @staticmethod
    def set_types():
        types = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other'
        ]

        for style in types:
            ShoeType.objects.create(style=style)

    def handle(self, *args, **options):
        self.set_colors()
        self.set_types()
