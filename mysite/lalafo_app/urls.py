from .views import (CategoryListView, ProductListView,
                    ProductCreateView, ProductDetailView,
                    ProductUpdateView, ProductDeleteView, MarchListView)
from django.urls import path

urlpatterns = [
    path('', MarchListView.as_view(), name='march_list')
    # path('category/', CategoryListView.as_view(), name='category_list'),
    # path('', ProductListView.as_view(), name='product_list'),
    # path('create/', ProductCreateView.as_view(), name='product_create'),
    # path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    # path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')

]