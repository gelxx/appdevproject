from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model= User
		fields = ('username','email','password2','password2')


class NotesForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = '__all__'

