from django.db import models

class Example(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.FileField(blank=True, null=True)
	cost = models.CharField(max_length=15)

	def __str__(self):
		return self.title