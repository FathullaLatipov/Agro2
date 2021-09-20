from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from neo.views import NeonTemplateView, NeonsTemplateView, Neon1TemplateView

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += i18n_patterns(
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('profile/', include('users.urls', namespace='profile')),
    path('products/', include('products.urls', namespace='products')),
    path('neo/', include('neo.urls', namespace='neo'),),
    path('neo1/', NeonTemplateView.as_view()),
    path('neo2/', NeonsTemplateView.as_view()),
    path('neo3/', Neon1TemplateView.as_view()),
    path('', include('pages.urls', namespace='contact')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)