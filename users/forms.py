from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


class RegisterForm(forms.Form):

    first_name = forms.CharField(max_length= 20, widget= forms.TextInput(attrs={'placeholder':'İsim'}),label='')
    last_name = forms.CharField(max_length= 20, widget= forms.TextInput(attrs={'placeholder':'Soyisim'}),label='')
    username = forms.CharField(max_length= 20, widget= forms.TextInput(attrs={'placeholder':'Kullanıcı Adı'}),label='')
    email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'Email'}),label='')
    password = forms.CharField(max_length= 16, min_length= 8, widget= forms.PasswordInput(attrs={'placeholder':'Şifre'}),label='')
    confirm = forms.CharField(max_length= 16, min_length= 8, widget= forms.PasswordInput(attrs={'placeholder':'Şifre Doğrula'}),label='')

    def clean(self):

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password != confirm:

            self.add_error('confirm', "Password does not match")

        elif '@' in username:

            self.add_error('username', "You can't @ in your username")

        elif User.objects.filter(username= username):

            self.add_error('username', "There is this account aıready")

        elif User.objects.filter(email= email):

            self.add_error('email', "There is this account aıready")


class LoginForm(forms.Form):

    username = forms.CharField(max_length= 100, widget= forms.TextInput(attrs={'placeholder':'Kullanıcı Adı yada email'}),label='')
    password = forms.CharField(max_length= 30, min_length= 8, widget= forms.PasswordInput(attrs={'placeholder':'Şifre'}),label='')

