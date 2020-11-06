from django.contrib import admin
from .models import Userinfo, bills, transactions

admin.site.register(Userinfo)
admin.site.register(bills)
admin.site.register(transactions)

# Register your models here.
