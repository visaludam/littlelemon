# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Booking(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	date = models.DateField()
	time = models.TimeField()
	number_of_guests = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.name} - {self.date} {self.time}"


class Menu(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	is_available = models.BooleanField(default=True)

	def __str__(self):
		return self.title
