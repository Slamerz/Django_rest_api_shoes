from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=25)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return self.brand
