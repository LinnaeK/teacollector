from django.forms import ModelForm
from .models import Drinking

class DrinkingForm(ModelForm):
    class Meta:
        model = Drinking
        fields = ['date', 'time', 'feeling']