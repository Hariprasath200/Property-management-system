from django.contrib import admin
from .models import Location, Bus, Hotel, DepositCenter

admin.site.register(Location)
admin.site.register(Bus)
admin.site.register(Hotel)
admin.site.register(DepositCenter)
