from django.core import validators
from django import forms
from .models import Task

class TaskRegistration(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            #'status' : forms.BooleanField(attrs={'class':'form-control'}),
        }