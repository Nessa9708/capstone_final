from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('get_dealers/', views.get_dealers, name='get_dealers'),
    path('get_dealers/<str:state>/', views.get_dealers, name='get_dealers_by_state'),
     path('get_dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer'),
    path('get_dealer_reviews/<int:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
]
