from django.urls import path
from . import views
from .views import stats_view, edit_user, change_password

urlpatterns = [
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("information/", stats_view, name="information"),
    path("edit/", edit_user, name="edit_user"),
    path("change-password/", change_password, name="change_password"),
]
