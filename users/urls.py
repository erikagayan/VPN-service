from django.urls import path
from . import views
from .views import stats_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('information/', stats_view, name='information'),
]
