from django.contrib import admin
from .models import Category, Company, Slot, Day, Address


class DayAdmin(admin.ModelAdmin):
	list_display = ['name', 'company']
class SlotAdmin(admin.ModelAdmin):
	list_display = ['day', 'start_time']




admin.site.register(Category)	
admin.site.register(Company)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Address)



