from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

@login_required
def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    if pizza.owner != request.user:
        raise Http404

    toppings = pizza.topping_set
    comments = pizza.comment_set
    context = {'pizza':pizza, 'toppings': toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

@login_required
def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            if pizza.owner == request.user:
                comment.save()
                form.save()
                return redirect('pizzas:pizza', pizza_id=pizza_id)
            else:
                print("Unauthorized Access")
                raise Http404

    context = {'form': form, 'pizza':pizza}
    return render(request, 'pizzas/comment.html', context)

@login_required
def edit_comment(request, comment_id):
    """Edit an existing comment."""
    comment = Comment.objects.get(id=comment_id)
    pizza = comment.pizza

    if pizza.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza.id)
    
    context = {'comment': comment, 'pizza':pizza, 'form':form}
    return render(request, 'pizzas/edit_comment.html', context)