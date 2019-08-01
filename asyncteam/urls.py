from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from timeline import views as timeline_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/timeline/favicon/favicon.ico')),
    path('accounts/', include('allauth.urls')),
    path('timeline/', include('timeline.urls')),
    path('', timeline_views.home, name='home'),
]
