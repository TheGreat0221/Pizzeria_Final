from django.shortcuts import render, redirect
from .models import Pizza, Topping

# Create your views here.

def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    toppings = pizza.topping_set
    context = {'pizza':pizza, 'toppings': toppings}

    return render(request, 'pizzas/pizza.html', context)

##def toppings(request):
##    toppings = Topping.objects.order_by('date_added')
##    context = {'toppings':toppings}
##    return render(request, 'pizzas/toppings.html', context)