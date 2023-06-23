from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm) :
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Username'}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Password'}))
    
class SignupForm(UserCreationForm) :
    class Meta : 
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Username'}))
    email = forms.CharField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Email'}))
    password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Password'}))
    password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Confirm Password'}))
    
    
    