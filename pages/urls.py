from django.urls import path
from .views import HomePageView
from .views import about

urlpatterns = [
    path("",HomePageView.as_view(),name='home'),
    path('about/',about.as_view(),name="home/about"),
]
