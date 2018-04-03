from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True,help_text='الزامی')
    last_name = forms.CharField(max_length=50,required=True,help_text='الزامی')
    email = forms.EmailField(max_length=254,required=True,help_text='الزامی')
    class Meta:
        model = User
        fields=('first_name','last_name','username','password1','password2','email')