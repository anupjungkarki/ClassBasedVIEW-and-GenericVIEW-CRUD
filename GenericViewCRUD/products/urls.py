from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateProductView.as_view(), name='create'),
    path('list/', views.ListProductView.as_view(), name='list'),
    path('update/<int:pk>', views.UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteProductView.as_view(), name='delete'),
    path('index/', views.ProductShowView.as_view(), name='index'),
]
