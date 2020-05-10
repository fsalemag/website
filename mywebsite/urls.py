from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("home.urls")),
    path('trips/', include("album.urls")),
    path('admin/', admin.site.urls),
]
