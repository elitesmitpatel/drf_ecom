from django.urls import path ,include
from .views import CustomerListCreateView, CustomerRetriveUpdateDestroyView


app_name = 'eapp'

urlpatterns = [
    path('customer/',CustomerListCreateView.as_view(),name='customer-list'),
    path('customer/create/',CustomerListCreateView.as_view(),name='customer-create'),
    path('customer/<int:pk>/',CustomerRetriveUpdateDestroyView.as_view(),name='customer-retrive-update-destroy'),

    
]
