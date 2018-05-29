from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('home/', views.home, name = "homepage"),
    path('mobile_solutions/', views.mobilesolutions, name = "mobilesolutions"),
    path('web_solutions/', views.websolutions, name = "websolutions"),
    path('payment/', views.payment, name = "payment"),
    path('services/', views.services, name = "services"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('blog/', views.blog, name = "blog"),
    path('contactcomplete/', views.contactcomplete, name = "contactcomplete"),
]
