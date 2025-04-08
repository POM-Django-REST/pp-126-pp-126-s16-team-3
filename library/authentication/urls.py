from django.urls import path
from .views import index, logout_view

app_name = "authentication"
urlpatterns = [
    path("", index, name="index"),
    path("login/", index, name="login"),
    path("logout/", logout_view, name="logout"),
]
