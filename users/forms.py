from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from users.models import CustomUser


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    """Форма для редактирования профиля"""

    class Meta:
        model = Profile
        fields = [
            'avatar', 'birth_date',
            'city', 'address', 'postal_code',
            'email_notifications', 'sms_notifications'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'avatar': 'Аватар',
            'birth_date': 'Дата рождения',
            'city': 'Город',
            'address': 'Адрес доставки',
            'postal_code': 'Индекс',
            'email_notifications': 'Получать email-рассылки',
            'sms_notifications': 'Получать SMS-уведомления',
        }