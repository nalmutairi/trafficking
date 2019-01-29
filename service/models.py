from django.db import models
from django.contrib.auth.models import User



# class User(AbstractUser):
# 	pass

class Company(models.Model):
	name = models.CharField(max_length = 100)
	categorystuff = models.CharField(max_length = 100)
	desc = models.TextField()
	logo = models.ImageField()
	slogan = models.CharField(max_length = 300, blank = True, null = True)


	def __str__(self):
		return self.name


class Category(models.Model):
	company = models.ForeignKey(Company, on_delete= models.CASCADE)
	name = models.CharField(max_length = 100)


class Day(models.Model):
	name = models.DateField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name = 'days')

	def __str__(self):
		return "Day: %s, Company: %s" % (self.name, self.company.name)

class Slot(models.Model):
	day = models.ForeignKey(Day, on_delete= models.CASCADE, related_name='slots')
	start_time = models.TimeField()
	end_time = models.TimeField()
	is_available = models.BooleanField()


class Appointment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'appointments', null=True, blank=True)
	slot = models.OneToOneField(Slot, on_delete = models.CASCADE)

	def __str__(self):
		return self.slot.day.company.name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)
	phone = models.CharField(max_length = 15)

	def __str__(self):
		return self.first_name


class Address(models.Model):
	profile = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='addresses')
	area = models.CharField(max_length = 100)
	block = models.CharField(max_length = 5)
	street = models.CharField(max_length = 50)
	house = models.CharField(max_length = 5)
	jaada = models.CharField(max_length = 5)


	def __str__(self):
		return self.area


