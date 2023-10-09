from django import forms
from django.db import models
from .models import User, SportsField


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.EmailField(label='Email')
    address = forms.CharField(max_length=255, label='Address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class ReservationForm(forms.Form):
    field = forms.ModelChoiceField(
        queryset=SportsField.objects.all(),
        empty_label="Select a field",
        label="Field"
    )
    date = forms.DateField(label="Date")
    time = forms.TimeField(label="Time")
