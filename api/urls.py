from django.urls import path
from .views import ProductList, ProductDetail
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title="Test Shop API",
    description="API for all things …",
    version="1.0.0",
)

urlpatterns = [
    path('', schema_view, name='openapi-schema'),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]
