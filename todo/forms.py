from django.forms import ModelForm, TextInput
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description']
        widgets = {'task': TextInput(attrs={
                'class': 'form-control',
                'name': 'task',
                'id': 'task',
                'placeholder': 'Task'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'name': 'description',
                'id': 'description',
                'placeholder': 'Description'
            })
            }

class DoneForm(ModelForm):
    done = forms.BooleanField()