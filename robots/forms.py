from django.forms import ModelForm
from .models import Robot


class ValidationForm(ModelForm):
    class Meta:
        model = Robot
        fields = ['version', 'model', 'created']
