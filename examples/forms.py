from django import forms
from .models import Example

class InputForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ["title", "description", "image"]
