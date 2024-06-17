from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('treatments/', views.treatments, name='treatments'),
    path('location/', views.location, name='location'),
]