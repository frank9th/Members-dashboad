from django.db import models

# Create your models here.

class Board(models.Model):
	FirstName = models.CharField(max_length=200)
	LastName =  models.CharField(max_length=600)
	Email = models.CharField(max_length=200)
	Gender = models.CharField(max_length=20)
	Track = models.CharField(max_length=100)
	Language = models.CharField(max_length=100)
	Point = models.CharField(max_length=20)

	def __str__(self):
		return self.name