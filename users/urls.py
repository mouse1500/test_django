'''Определение схемы URL для пользователей'''

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Включить URL автоматизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации пользователя
    path('register/', views.register, name='register'),
]