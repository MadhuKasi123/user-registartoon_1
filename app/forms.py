from django import forms
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['adderss','profile_pic']
