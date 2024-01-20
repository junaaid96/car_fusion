from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

]