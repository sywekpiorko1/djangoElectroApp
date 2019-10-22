from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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

    # POST
    
    if request.method == 'POST':

        # create forms instances and populate fileds with data from current user and user.profile instances but also pass POST data including image in p_form 
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 

            # create success messages using f string
            messages.success(request, f'Your account has been updated')

            # redirect user to his profile page after update
            return redirect('profile')   

    else:
    
    # GET
        
        # create forms instances and populate fileds with data from current user and user.profile instances
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # pass forms to ours template with context dictionary with keys to be accessed within template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # pass context into template > using combined {{ u_form }} and {{ p_form }}
    return render(request, 'accounts/profile.html', context)
