from django.urls import path
from . import views

urlpatterns = [   
    path('', views.LVfunction, name='home'),
    path('infoprodotto',views.infoProdotto, name='infoprodotto')
]