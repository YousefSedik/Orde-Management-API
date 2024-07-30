from django.contrib import admin
from . import models 
from user.models import CustomUser
# Register your models here.
admin.site.register(models.Cart)
admin.site.register(models.Product)
admin.site.register(models.OrderItem)
admin.site.register(CustomUser)
