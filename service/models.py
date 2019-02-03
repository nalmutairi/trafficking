from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length = 100)
	pic = models.ImageField(null = True, blank = True)

	def __str__(self):
		return self.name

class Company(models.Model):
	name = models.CharField(max_length = 100)
	category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name = 'categories')
	desc = models.TextField()
	logo = models.ImageField(null = True, blank = True)
	slogan = models.CharField(max_length = 300, blank = True, null = True)
	
	def __str__(self):
		return self.name

class Day(models.Model):
	name = models.DateField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name = 'days')


class Slot(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'appointments', null=True, blank=True)
	day = models.ForeignKey(Day, on_delete= models.CASCADE, related_name='slots')
	start_time = models.TimeField()
	end_time = models.TimeField()


class Address(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='addresses')
	phone = models.CharField(max_length = 15)
	area = models.CharField(max_length = 100)
	block = models.CharField(max_length = 5)
	street = models.CharField(max_length = 50)
	house = models.CharField(max_length = 5)
	jaada = models.CharField(max_length = 5, null = True, blank = True)


	def __str__(self):
		return self.area


