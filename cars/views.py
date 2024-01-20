from django.views.generic import DetailView
from .models import Car

class CarDetailsView(DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'

    