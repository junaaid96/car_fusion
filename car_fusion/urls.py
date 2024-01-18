from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # path('cars/', include('cars.urls')),
    # path('brands/', include('brands.urls')),
    path('customers/', include('customers.urls')),
    # path('orders/', include('orders.urls')),
]
