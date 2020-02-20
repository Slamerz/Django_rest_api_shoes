from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_shoes import models


class ManufacturerSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['id', 'name', 'website']


class ShoeTypeSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType
        fields = ['id', 'style']


class ShoeColorSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor
        fields = ['id', 'color']


class ShoeSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = models.Shoe
        fields = [
            'id',
            'size',
            'brand',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]
