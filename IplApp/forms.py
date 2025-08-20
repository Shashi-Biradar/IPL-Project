from django import forms
from django.contrib.auth.models import User
from .models import Player,Stadium,Profile


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['name','age','role','nationality','franchise','photo']

class StadiumForm(forms.ModelForm):

    class Meta:
        model = Stadium
        fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone_number','address','profile_photo']
