from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_items_list, name='warehouse-items'),
]