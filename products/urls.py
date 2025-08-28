from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('catalog/', views.ProductListView.as_view(), name='catalog'),
    path('category/<int:category_id>/', views.ProductListView.as_view(), name='category'),
    path('page/<int:page>/', views.ProductListView.as_view(), name='paginator'),
]
