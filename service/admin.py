from django.contrib import admin
from .models import Company, Slot, Day, Appointment, Profile


class SlotAdmin(admin.ModelAdmin):
	list_display = ['day', 'start_time']
admin.site.register(Company)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Day)
admin.site.register(Appointment)
admin.site.register(Profile)


