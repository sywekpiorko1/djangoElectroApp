from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    
    # POST
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            # create success messages using f string
            messages.success(request, f'Account created for {username}!')

            # redirect user to other page after successful registration
            return redirect('warehouse-items')

    else: 

    # GET

        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})
