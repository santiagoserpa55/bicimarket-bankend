from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from . import views
from .views import MyTokenObtainPairView
urlpatterns = [
    #path('login', views.login, name='login'),
    path('login', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('add', views.newCustomer, name='newCustomer'),
    path('get', views.getCustomers, name='getCustomers'),
    path('getOneCustomer/<int:id>', views.getOneCustomer, name='getOneCustomer'),
    path('updateCustomer/<int:id>', views.updateCustomer, name='updateCustomer'),
    path('deleteCustomer/<int:id>', views.deleteCustomer, name='deleteCustomer'),
    path('addBike', views.newBike, name='addBike'),
    path('getAllBikes', views.getAllBikes, name='getAllBikes'),
    path('getOneBike/<int:id>', views.getOneBike, name='getOneBike'),
    path('updateBike/<int:id>', views.updateBike, name='updateBike'),
    path('deleteBike/<int:id>', views.deleteBike, name='deleteBike'),
]