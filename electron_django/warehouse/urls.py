from django.urls import path
from .views import (
    warehouse_items_list,
    warehouse_detail_view,
    warehouse_create_view,
)

urlpatterns = [
    path('', warehouse_items_list, name='warehouse-items'),
    path('<int:pk>/', warehouse_detail_view, name='warehouse-items-detail'),
    path('add/', warehouse_create_view, name='warehouse-items-create'),
]