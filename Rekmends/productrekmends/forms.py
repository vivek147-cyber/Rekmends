from django.db import models
from django import  forms 
from .models import Review

class Reviewfrom(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ["name","email","message"]

