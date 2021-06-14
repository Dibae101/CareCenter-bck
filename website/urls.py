from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("tour/", views.tour, name="tour"),
    path("contact/", views.contact, name="contact"),
    path("carrer/", views.HomeView.as_view(), name="carrer")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
