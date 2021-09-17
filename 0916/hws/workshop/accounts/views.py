from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserChangeForm


@require_safe
def index(request):
    User = get_user_model()
    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm(request)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    
    return redirect('accounts:index')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def chg_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/chg_pw.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    
    return redirect('accounts:index')