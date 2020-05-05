from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'), ## home page
    #path('Pizzas', views.pizzas, name='pizzas'), ## pizza page
    #path('Toppings', views.toppings, name='toppings'), ## topping page
]