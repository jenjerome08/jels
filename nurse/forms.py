from django.forms import ModelForm
from .models import Respondent, Vaccine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RespondentForm(ModelForm):
	class Meta:
		model = Respondent
		fields = '__all__'

class VaccineForm(ModelForm):
	class Meta:
		model = Vaccine
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

