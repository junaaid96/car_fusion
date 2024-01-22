from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('filter_by_brand/<int:brand_id>/', views.filter_by_brand, name="filter_by_brand"),
    path('cars/', include('cars.urls')),
    path('customers/', include('customers.urls')),
    path('orders/', include('orders.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
