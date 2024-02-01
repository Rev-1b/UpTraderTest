from django.urls import path
from draw_menu.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='index')
]