from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path('<int:dest_id>',views.details,name='details')
]
