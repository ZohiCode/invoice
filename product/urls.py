from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path("add", views.add_product, name="add_product"),
    path("update/<int:id>", views.update_product, name="update_product"),
    path("delete/<int:id>", views.delete_product, name="delete_product"),
]