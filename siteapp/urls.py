# siteapp/urls.py
from django.urls import path
from . import views

# If you want to reuse the get_cars view you already built in vehicles:
# from vehicles.views import get_cars

urlpatterns = [
    # basic pages you already have
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # auth pages if you added them
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register, name='register'),

    # If you want to expose your cars JSON here, uncomment the import above:
    # path('get_cars/', get_cars, name='get_cars'),

    # (For Part C later, you can add the proxy endpoints here)
    # path('get_dealers/', views.get_dealerships, name='get_dealers'),
    # path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),
    # path('get_dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),
    # path('get_reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
    # path('add_review/', views.add_review, name='add_review'),
]
