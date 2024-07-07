import secrets
import string

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()
            send_mail(
                'Password Reset',
                f'Ваш новый пароль: {new_password}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False, )
            return redirect('users:login')
        except User.DoesNotExist:
            error_message = 'Пользователь с таким адресом электронной почты не существует.'
    else:
        error_message = ''

    return render(request, 'users/reset_password.html', {'error_message': error_message})


def logout(request):
    return redirect('users:login')

# def generate_random_password(length=12, include_special_chars=True):
#     characters = string.ascii_letters + string.digits
#     if include_special_chars:
#         characters += string.punctuation
#
#     password = ''.join(secrets.choice(characters) for i in range(length))
#     return password
