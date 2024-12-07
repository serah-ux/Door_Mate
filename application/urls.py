"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path

from application import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('site/', views.SiteView, name='site'),
    path('reg/', views.RegView, name='reg'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book, name='book'),
    path('profile/', views.profile, name='profile'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('print/<int:id>/', views.print_appointment, name='print_appointment'),
    path('appointmentapi/', views.appointmentapi, name='appointmentapi'),
    path('mpesaapi/', views.mpesaapi, name='mpesaapi'),

]


