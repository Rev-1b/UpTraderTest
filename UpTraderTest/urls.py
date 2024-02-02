from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('draw_menu.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
