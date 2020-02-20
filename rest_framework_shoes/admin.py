from django.contrib import admin
from rest_framework_shoes import models


admin.site.register(models.Manufacturer)
admin.site.register(models.ShoeType)
admin.site.register(models.ShoeColor)
admin.site.register(models.Shoe)

