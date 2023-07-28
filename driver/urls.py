from django.urls import path

from driver import views

urlpatterns = [
    path('', views.drivers, name='all_drivers'),
]