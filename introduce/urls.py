from django.urls import path
from . import views

urlpatterns = [
    path('introduce/', views.test_introduce,name='test'),
    
]