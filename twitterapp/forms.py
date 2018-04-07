from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Feed

class SignupUserForm(UserCreationForm):

    first_name = forms.CharField(max_length=30,min_length=3,required=True,help_text='الزامی',
                                 widget=forms.TextInput(attrs={'class':'form-control','autofocus':'true'}))
    last_name = forms.CharField(max_length=50,min_length=3,required=True,help_text='الزامی',
                                widget=forms.TextInput(attrs={'class' : 'form-control',}))
    email = forms.EmailField(max_length=254,min_length=6,required=True,help_text='الزامی',
                             widget=forms.TextInput(attrs={'class' : 'form-control',}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password1','password2','email',)
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control',}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control',}),
            'password2': forms.PasswordInput(attrs={'class':'form-control',}),
        }

    def claen(self):
        cleaned_date = super(SignupUserForm,self).clean()
        first_name =  cleaned_date.get('first_name')
        last_name = cleaned_date.get('last_name')
        email = cleaned_date.get('email')
        username = cleaned_date.get('username')
        password1 = cleaned_date.get('password1')
        password2 = cleaned_date.get('password2')
        if not first_name and not last_name and not email and not username and not password1 and not password2:
            raise forms.ValidationError('هیچ یک از فیلد ها نمیتوانند خالی باشند')

class FeedForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ('post',)
        widgets = {
            'post': forms.Textarea(attrs={'class':'form-control','draggable':'false'}),
        }

        def clean(self):
            cleaned_data = super(FeedForm, self).clean()
            post = cleaned_data.get('post')
            if not post:
                raise forms.ValidationError('باید چیزی نوشته باشید')
