from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile


# we create UserRegisterForm that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # we add extra field, required is true by default
    email = forms.EmailField()

    # we specify the model that form will interact with
    class Meta:
        model = User    # so save() will save fields to User model
        # we specify fields and order to be shown in form
        fields = ['username', 'email', 'password1', 'password2']
        

# we create a model form that will work with specific database model > that will update user model
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# to update profile picture we have to create additional form on Profile model
class ProfileUpdateForm(forms.ModelForm):
    
    # we dont add additional fields so skip to Meta
    class Meta:
        model = Profile
        fields = ['image']



