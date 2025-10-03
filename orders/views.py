import stripe
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from cart.models import Cart
from common.views import TitleMixin

from .forms import OrderForm
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'create_order.html'
    form_class = OrderForm
    title = 'Оформление заказа'
    success_url = reverse_lazy('orders:create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        carts = Cart.objects.filter(user=self.request.user, )
        line_items = [{'price': cart.product.stripe_product_price_id, 'quantity': cart.quantity, } for cart in carts]
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=settings.SUCCESS_URL_STRIPE,
            cancel_url=settings.CANCEL_URL_STRIPE,
        )
        order = Order.objects.get(id=self.object.id)
        order.order_items_history(carts)
        return HttpResponseRedirect(checkout_session.url, status=303)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)


class OrderSuccessTemplateView(TemplateView):
    template_name = 'order_success.html'


class OrderCanceledTemplateView(TemplateView):
    template_name = 'order_canceled.html'
