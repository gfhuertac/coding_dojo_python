from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from .models import Order, Product

def index(request):
  context = {
    "all_products": Product.objects.all()
  }
  return render(request, "store/index.html", context)

def checkout(request):
  quantity_from_form = int(request.POST["quantity"])
  product_from_form = int(request.POST["product"])
  product = Product.objects.get(id=product_from_form)
  total_charge = quantity_from_form * product.price
  print("Charging credit card...")
  order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
  return redirect('thank_you', id=order.id)

def thank_you(request, id:int):
  order = Order.objects.get(id=id)
  total_qty = Order.objects.aggregate(Sum('quantity_ordered'))
  total_price = Order.objects.aggregate(Sum('total_price'))
  context = {
    'order': order,
    'total_qty': total_qty,
    'total_price': total_price,
  }
  return render(request, "store/thank_you.html", context=context)
