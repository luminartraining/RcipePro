from django.forms import ModelForm
# User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)
    def clean(self):
        print("inside clean validate user and password")



class ProfileCreateForm(ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:

        model=Profile

        fields=["user","pofile_pic","bio","birth_date"]


