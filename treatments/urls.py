from django.urls import path
from . import views

urlpatterns = [
    path('treatments/', views.treatments_view, name='treatments'),
]