from rest_framework import viewsets
from rest_framework_shoes import models, serializers


class ManufacturerView(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializers


class ShoeTypeView(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializers


class ShoeColorView(viewsets.ModelViewSet):
    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializers


class ShoeView(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializers
