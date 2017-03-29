from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'school', 'graduate', 'nation', 'keywords')