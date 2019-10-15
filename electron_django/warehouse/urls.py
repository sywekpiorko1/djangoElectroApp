from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_items_list, name='warehouse-items'),
    path('add/', views.create_an_item, name='warehouse-items-create'),
]