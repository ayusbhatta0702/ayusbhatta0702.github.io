from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "Mahimail_home"),
    path('about/', views.about, name = "Mahimail_about")
]