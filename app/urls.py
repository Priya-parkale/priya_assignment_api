from django.urls import path
from app import views

urlpatterns = [
    path('', views.OpenWeather.as_view(), name="apiView"),
]
