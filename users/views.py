from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from users.forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})



@login_required
def profile_view(request):
    """Просмотр профиля текущего пользователя"""
    profile = request.user.profile  # OneToOneField дает доступ!
    context = {
        'profile': profile,
        'title': 'Мой профиль'
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_edit(request):
    """Редактирование профиля"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Профиль успешно обновлен!')
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'title': 'Редактирование профиля'
    }
    return render(request, 'users/profile_edit.html', context)
