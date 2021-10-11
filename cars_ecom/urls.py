from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'cars_ecom'

router = routers.DefaultRouter()
router.register('api/clients', ClientsView, basename='clients')
router.register('api/cars', CarsView, basename='cars')
router.register('api/orders', OrdersView, basename='orders')
router.register('api/extend-orders', ExtendOrdersView, basename='extends')
router.register('api/users', UsersView, basename='users')
router.register('api/order-filter', OrderFilterView, basename='order-filter')
router.register('api/cars-filter', CarsFilterView, basename='cars-filter')
router.register('api/client-filter', ClientFilterView, basename='client-filter')


urlpatterns = [
    path('', include(router.urls)),
]