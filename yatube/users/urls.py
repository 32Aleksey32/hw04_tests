from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView)
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Регистрация
    path('signup/', views.SignUp.as_view(), name='signup'),

    # Авторизоваться
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),

    # Выйти
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logged_out.html'),
        name='logout'
    ),

    # Смена пароля
    path('password_change/',
         PasswordChangeView.as_view(
             template_name='users/password_change_form.html'),
         name='password_change_form'
         ),

    # Сообщение об успешном изменении пароля
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'),
         name='password_change_done'
         ),

    # Восстановление пароля через email
    path("password_reset/",
         PasswordResetView.as_view(
             template_name="users/password_reset_form.html"),
         name="password_reset_form",
         ),

    # Сообщение об успешном восстановлении пароля
    path('reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),

    # Вход по ссылке для восстановления пароля
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm'),
         name='password_reset_confirm'
         ),

    # Сообщение об отправке ссылки для восстановления пароля
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'
         ),

]
