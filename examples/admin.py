from django.contrib import admin
from .models import Example

class ExampleAdmin(admin.ModelAdmin):
	list_display = ['__str__']
	search_fields = ['title', 'cost']
	
	class Meta:
		model = Example

admin.site.register(Example)