
from django.forms import ModelForm
from .models import Squirrels
class Form(ModelForm):
    class Meta:
        model = Squirrels
        fields = '__all__'
