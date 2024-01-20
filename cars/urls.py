from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>', views.CarDetailsView.as_view(), name='car_details'),
]
