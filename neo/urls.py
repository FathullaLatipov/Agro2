from django.urls import path

from neo.views import NeoTemplateView

app_name = 'neo'

urlpatterns = [
    path('', NeoTemplateView.as_view(), name="neo")
]