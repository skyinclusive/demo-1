from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 50)
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class StudentForm(forms.ModelForm):
	class Meta:
		model = models.Student
		fields = "__all__"
        # exclude = ["/"]