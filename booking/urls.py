from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_form, name='booking_form'),
    path('/book-details/',views.booking_form,name='book_details')
]
