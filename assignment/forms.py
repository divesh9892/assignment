from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from assignment.models import FileUpload


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']



class FileForm(forms.ModelForm):
   
  class Meta:
        model = FileUpload
        fields = ('desc', 'file',)