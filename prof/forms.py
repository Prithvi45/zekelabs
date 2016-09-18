from django import forms
from django.forms import ModelForm
from .models import UserProfile 
from django.db import models
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'