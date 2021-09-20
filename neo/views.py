from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class NeoTemplateView(TemplateView):
    template_name = 'neo.html'


class NeonTemplateView(TemplateView):
    template_name = 'neopage/neo1.html'


class NeonsTemplateView(TemplateView):
    template_name = 'neopage/neo2.html'


class Neon1TemplateView(TemplateView):
    template_name = 'neopage/neo3.html'
