from unittest.util import _MAX_LENGTH
from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth import password_validation
from .models import Member
from django.contrib.auth.forms import AuthenticationForm, UsernameField
class FormRegisterForm(forms.Form):
    username = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'placeholder':"Enter your Username"}))
    funame = forms.CharField(
                            max_length=100,
                            label="Full Name",
                            widget=forms.TextInput(attrs={'placeholder':"Enter your Full Name"}))
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'placeholder':"Enter your Email Address"}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':"Enter your Phone Number"}))
    password = forms.CharField(max_length=20 , widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password','placeholder':"Enter the Password"}))
    confirm_Password = forms.CharField(max_length=20, label="Confirm Password", widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password','placeholder':"Enter the Confirm Password"}))

    class Meta:
        model = Member
        fields = ["username","funame","email","mobile","password"]

class LoginForm(AuthenticationForm):
    username = UsernameField( 
        label="Username",
        widget=forms.TextInput(attrs={"autofocus": True, 'class':'form_control','placeholder':"Enter your Username"}))

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form_control','placeholder':"Enter your Password"}),
    )