from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LogoutView
from common.views import TitleMixin
from orders.models import Order
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification

User = get_user_model()


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Verification'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('products:home'))


class UserProfileView(LoginRequiredMixin, TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(initiator_id=self.request.user.id)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class UserLoginView(SuccessMessageMixin, TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_message = 'Вы вошли в аккаунт!'
    title = 'Login'


class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('products:home')
    success_message = 'Вы успешно зарегестрировались!'
    title = 'Registration'

class UserLogoutView(LogoutView):
    success_message = 'Вы вышли из аккаунта!'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
