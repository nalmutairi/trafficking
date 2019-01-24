from django.contrib import admin
from django.contrib.auth.models import User
from .models import Company, Slot, Day, Appointment


class SlotAdmin(admin.ModelAdmin):
	list_display = ['day__name', 'start_time']
admin.site.register(Company)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Day)
admin.site.register(Appointment)
admin.site.register(User)

