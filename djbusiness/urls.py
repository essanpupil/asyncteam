from django.urls import path
from django.views.generic import RedirectView

from .views import home, PageView

app_name = 'djbusiness'
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/djbusiness/favicon/favicon.ico')),
    path('<slug:slug>', PageView.as_view(), name='page'),
    path('', home, name='home'),
    ]
