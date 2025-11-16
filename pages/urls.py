



# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView,SasPageView # new
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('sas/', SasPageView.as_view(), name='sas'), # new
]
