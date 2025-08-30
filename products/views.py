from django.views.generic import ListView, TemplateView, DetailView

from common.views import TitleMixin

from .models import Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'index.html'
    title = 'Home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Product.objects.all()
        context['popular_products'] = queryset[:4]
        return context

class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'catalog.html'
    paginate_by = 6
    title = 'Catalog'
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailView(TitleMixin, DetailView):
    title = 'Product'
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


