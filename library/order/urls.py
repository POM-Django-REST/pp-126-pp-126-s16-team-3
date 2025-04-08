from django.urls import path
from .views import index, single_order

app_name = 'order'

urlpatterns = [
    path('', index, name='index'),
    path('<int:order_id>/', single_order, name='single_order'),
]