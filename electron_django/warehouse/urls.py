from django.urls import path
from .views import (
    warehouse_items_list,
    warehouse_detail_view,
    warehouse_create_view,
    warehouse_update_view,
    warehouse_delete_view,
)

urlpatterns = [
    path('', warehouse_items_list, name='warehouse-items'),
    path('add/', warehouse_create_view, name='warehouse-items-create'),
    path('<int:pk>/', warehouse_detail_view, name='warehouse-items-detail'),
    path('<int:pk>/edit/', warehouse_update_view, name='warehouse-items-edit'),
    path('<int:pk>/delete/', warehouse_delete_view, name='warehouse-items-delete'),
]