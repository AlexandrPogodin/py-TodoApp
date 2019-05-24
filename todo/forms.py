from django.forms import ModelForm, TextInput
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description', 'author']
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
            }),
            'author': TextInput(attrs={
                'type': 'hidden',
                'name': 'author',
                'id': 'author',
            })
            }

class DoneForm(ModelForm):
    done = forms.BooleanField()