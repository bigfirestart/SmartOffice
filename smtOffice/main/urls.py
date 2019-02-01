from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('success',views.buy),
    path('buys',views.showBuys),
]
