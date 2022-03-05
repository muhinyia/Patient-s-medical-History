from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import HealthOfficer
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import HealthOfficer
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:

            auth.login(request, user)

            messages.success(request, 'You are Logged in Welcome ')
            if username == 'admin':
                return redirect('admins:index')

            else:

                return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html', )


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are Logged out')

    return redirect('accounts:login')


@login_required
def dashboard(request):
    user_id = request.user.id
    this_user = get_object_or_404(User, pk=user_id)
    officer = get_object_or_404(HealthOfficer, user=this_user)
    context = {'officer': officer, }
    return render(request, 'accounts/officers_dashboard.html', context)
