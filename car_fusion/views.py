from django.shortcuts import render
from cars.models import Car
from brands.models import Brand


def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    context = {'cars': cars, 'brands': brands}
    return render(request, 'home.html', context)

# sort by brand
def filter_by_brand(request, brand_id):
    brands = Brand.objects.all()
    cars = Car.objects.filter(brand=brand_id)
    context = {'cars': cars, 'brands': brands}
    return render(request, 'home.html', context)
