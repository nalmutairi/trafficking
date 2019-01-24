from django.db import models
from django.contrib.auth.models import User



# class User(AbstractUser):
# 	pass

class Company(models.Model):
	name = models.CharField(max_length = 100)
	category = models.CharField(max_length = 100)
	desc = models.TextField()
	logo = models.ImageField()


	def __str__(self):
		return self.name


class Day(models.Model):
	name = models.DateField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name = 'company')

	def __str__(self):
		return "Day: %s, Company: %s" % (self.name, self.company.name)

class Slot(models.Model):
	day = models.ForeignKey(Day, on_delete= models.CASCADE)
	start_time = models.TimeField()
	end_time = models.TimeField()
	is_available = models.BooleanField()



class Appointment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user', null=True, blank=True)
	slot = models.ForeignKey(Slot, on_delete = models.CASCADE, related_name = 'app_slot')


	def __str__(self):
		return self.slot.day.company.name



class Address(models.Model):
	area = models.CharField(max_length = 100)
	block = models.CharField(max_length = 5)
	street = models.CharField(max_length = 50)
	house = models.CharField(max_length = 5)
	jaada = models.CharField(max_length = 5)


	def __str__(self):
		return self.area

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)
	address = models.ForeignKey(Address, on_delete= models.CASCADE)
	phone = models.CharField(max_length = 15)

	def __str__(self):
		return self.first_name


