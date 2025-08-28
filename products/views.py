from django.views.generic import ListView, TemplateView

from common.views import TitleMixin

from .models import Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'index.html'
    title = 'Home'
    extra_context = {'popular_products': Product.objects.all()[:4]}


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
