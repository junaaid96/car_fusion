from django.shortcuts import render

# Create your views here.
def place_order(request):
    return render(request, 'place_order.html')