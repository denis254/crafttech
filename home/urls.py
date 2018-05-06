
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home.as_view()),
    path('home/', views.home.as_view()),
    path('webdesign/', views.webdesign.as_view()),
    path('seo/', views.seo.as_view()),
    path('smo/', views.smo.as_view()),
    path('webhost/', views.webhost.as_view()),
    path('domain/', views.domain.as_view()),
    path('about/', views.about.as_view()),
    path('contactcomplete/', views.contactcomplete.as_view()),
    path('contact/', views.contact, name = "contactus"),
    path('consultancy/', views.consultancyt.as_view())
]
