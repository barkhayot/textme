from django.shortcuts import render, redirect
from . models import Profile
from . forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully has been created')
            return redirect('loginPage')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')

    if request.user.is_authenticated == True:
        return redirect('home')

    return render(request, 'account/login.html')

@login_required(login_url='/loginpage')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


# User Account Function
@login_required(login_url='/loginpage')
def userAccount(request):
    profile = request.user.profile

    context = {
        'profile': profile
    }

    return render(request, 'account/userAccount.html', context)


@login_required(login_url='/loginpage')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form,
                'profile': profile}
    return render(request, 'account/profile_form.html', context)

