from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signupacc, name="signup"),
    path('login/',views.loginacc, name="login"),
    path('logout/',views.logoutacc, name='logout'),
]