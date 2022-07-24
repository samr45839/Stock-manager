from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(Order_Client)
admin.site.register(Client_Category)
admin.site.register(Provider)
admin.site.register(Product)