from django.urls import path
from customer_info import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('login_customer', views.login_user, name='login_customer'),
    path('login_page', views.login_page, name='login_page'),
    path('logout_customer', views.logout_user, name='logout_customer'),
]
