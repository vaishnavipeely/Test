from django.db import models

# Create your models here.


class Apimodel(models.Model):
	Quiz = models.CharField(max_length=100)
	sampletest =models.CharField(max_length=100)
	sleeping = models.CharField(max_length=100)
	playing = models.CharField(max_length=100)
	learning =models.CharField(max_length=100)
	
	def __str__(self):
		return self.playing