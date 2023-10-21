from django.contrib import admin
from .models import StoreStatus, StoreHours, StoreTimezone

admin.site.register(StoreStatus)
admin.site.register(StoreHours)
admin.site.register(StoreTimezone)
