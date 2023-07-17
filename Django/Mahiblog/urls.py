from django.urls import path
from . import views

#path('path that will be typed in the link bar', views.something, name = "something but unique")
urlpatterns = [
    path('', views.home, name = "Mahiblog_home"),
    path('about/', views.about, name = "Mahiblog_about")
    
]
