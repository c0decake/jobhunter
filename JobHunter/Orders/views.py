from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def orders(request):
    return render(request, 'Orders/orders.html')
