from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('success/', views.OrderSuccessTemplateView.as_view(), name='success'),
    path('canceled/', views.OrderCanceledTemplateView.as_view(), name='canceled'),
]
