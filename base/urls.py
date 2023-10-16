from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('buy/', views.buy, name="buy"),
    path('tickets/', views.tickets, name="tickets"),
]