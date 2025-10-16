from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from siteapp import urls as site_urls
from vehicles.views import get_cars  # <-- import the ONLY custom view we need here

urlpatterns = [
    path('admin/', admin.site.urls),

    # Static pages via templates (no siteapp.views needed)
    path('',        TemplateView.as_view(template_name='home.html'),    name='home'),
    path('about/',  TemplateView.as_view(template_name='about.html'),   name='about'),
    path('contact/',TemplateView.as_view(template_name='contact.html'), name='contact'),

    # API for Module 3 Part B
    path('get_cars/', get_cars, name='get_cars'),
    path('', include('siteapp.urls')),        # your static pages
    path('', include('dealerapp.urls')),  
]
