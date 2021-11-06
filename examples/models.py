from django.db import models

class Example(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.FileField(blank=False, null=True)

	def __str__(self):
		return self.title
