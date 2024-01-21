from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Car, Order


@login_required
def place_order(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    user = request.user
    order = Order.objects.create(
        customer=user,
        car=car,
        quantity=1,
        total_price=car.price,
        status='Sold'
    )
    order.save()
    car.quantity -= 1
    car.save()
    return render(request, 'order_details.html', {'order': order})
