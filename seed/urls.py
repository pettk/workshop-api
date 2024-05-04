from django.urls import path
from .views import SeedsList, SeedDetail

urlpatterns = [
    path('seeds/', SeedsList.as_view(), name='product-list-create'),
    path('seeds/<int:pk>/', SeedDetail.as_view(), name='product-detail'),
]
