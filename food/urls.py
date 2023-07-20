from django.urls import path
from .views.category import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
)

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view()),
    path('category/list/', CategoryListView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view()),
]

from .views.subcategory import (
    SubCategoryCreateView,
    SubCategoryDeleteView,
    SubCategoryDetailView,
    SubCategoryListView,
    SubCategoryUpdateView,
)

urlpatterns += [
    path('subcategory/create/', SubCategoryCreateView.as_view()),
    path('subcategory/list/', SubCategoryListView.as_view()),
    path('subcategory/detail/<int:pk>/', SubCategoryDetailView.as_view()),
    path('subcategory/update/<int:pk>/', SubCategoryUpdateView.as_view()),
    path('subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view()),
]

from .views.product import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

urlpatterns += [
    path('product/create/', ProductCreateView.as_view()),
    path('product/list/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
]

    
    