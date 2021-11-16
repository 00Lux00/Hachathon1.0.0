from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
]