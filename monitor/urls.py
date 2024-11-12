from django.urls import path
from .views import htop_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('htop/', htop_view, name='htop'),
]
