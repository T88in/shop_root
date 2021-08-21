from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ans/<slug:stok>/', answer),# name= zapros), #Страница redirect
    path('office/', office),

]