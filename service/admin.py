from django.contrib import admin
from .models import Company, Slot, Day, Appointment


admin.site.register(Company)
admin.site.register(Slot)
admin.site.register(Day)
admin.site.register(Appointment)

