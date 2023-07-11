from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='show'),
    path('numeric', views.numeric, name='numeric'),
    path('nominal', views.nominal, name='nominal'),
    path('ordinal', views.ordinal, name='ordinal'),
]
