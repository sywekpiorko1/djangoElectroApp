from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    
    # POST
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            # create success messages using f string
            messages.success(request, f'Your account has been created - You can now LogIn')

            # redirect user to other page after successful registration
            return redirect('login')

    else: 

    # GET

        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
