from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from products.forms import CommentModelForm
from products.utils import get_cart_data

from pages.forms import ContactModelForm
from products.models import ProductModel, CategoryModel, CategoryHomeModel


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    extra_context = {'title': 'Contact'}

    def get_success_url(self):
        return reverse('contact:contact')


class HomeView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Home'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.order_by('-pk')[:8]
        context['cats'] = CategoryModel.objects.order_by('-pk')[:1]

        return context


class AboutView(TemplateView):
    template_name = 'blog.html'
    extra_context = {'title': 'About'}


class LoginView(TemplateView):
    template_name = '/registration/login.html'
    extra_context = {'title': 'Login'}


class RegisterView(TemplateView):
    template_name = '/registration/registration_form.html'
    extra_context = {'title': 'Login'}


class FlipView(TemplateView):
    template_name = 'layouts/flip.html'


def registration_done(request):
    messages.add_message(request, messages.INFO, 'Success')
    return redirect(reverse('contact:register'))


class ProductOneTemplateView(TemplateView):
    template_name = 'products/product1.html'

class ProductTwoTemplateView(TemplateView):
    template_name = 'products/product_two.html'


class ProductThreeTemplateView(TemplateView):
    template_name = 'products/product_three.html'


class ProductFourTemplateView(TemplateView):
    template_name = 'products/product_four.html'


class ProductFiveTemplateView(TemplateView):
    template_name = 'products/product_five.html'


class ProductSixTemplateView(TemplateView):
    template_name = 'products/product_six.html'


class ProductSevenTemplateView(TemplateView):
    template_name = 'products/product_seven.html'


class ProductEightTemplateView(TemplateView):
    template_name = 'products/product_eight.html'


class ProductNightTemplateView(TemplateView):
    template_name = 'products/product_night.html'


class ProductTenTemplateView(TemplateView):
    template_name = 'products/product_ten.html'


class ProductElevenTemplateView(TemplateView):
    template_name = 'products/product_11.html'


class ProductTwelfTemplateView(TemplateView):
    template_name = 'products/product_12.html'


class FlipTemplateView(TemplateView):
    template_name = 'flip/flip1.html'