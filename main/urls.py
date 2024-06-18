from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discover/', views.discover_spa, name='discover_spa'),
    path('treatments/', views.treatments, name='treatments'),
]