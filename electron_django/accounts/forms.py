from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


# we create UserRegisterForm that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # we add extra field, required is true by default
    email = forms.EmailField()

    # we specify the model that form will interact with
    class Meta:
        model = User    # so save() will save fields to User model
        # we specify fields and order to be shown in form
        fields = ['username', 'email', 'password1', 'password2']
        


