from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item, OrderItem, Order
# Create your views here.

def products(request):

    context = {
        'items': Item.objects.all()
    }

    return render(request, "product.html", context)

def checkout(request):
        return render(request, "checkout.html")

class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ItemDetailView(DetailView):

    model = Item
    template_name = "product.html"

def Home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)

def anadir_al_carro(request,slug):
    item=get_object_or_404(Item, slug=slug)
    order_item= OrderItem.objects.create(item=item)
    order_qs= Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        #comprobar si order item esta en order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.cantidad += 1
            order_item.save()
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product",   slug  = slug)
