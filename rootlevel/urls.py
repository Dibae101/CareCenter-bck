from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("kyakadmin/", admin.site.urls),
    path("", include("website.urls")),
]
