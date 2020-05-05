from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'), ## home page
    path('pizzas', views.pizzas, name='pizzas'), ## pizza page
    path('pizzas/<int:pizza_id>/', views.pizza,name="pizza"), ## drill down into each pizza to see toppings
    ##path('toppings', views.toppings, name='toppings'), ## topping page
]