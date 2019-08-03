from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from company import views as company_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/company/favicon/favicon.ico')),
    path('accounts/', include('allauth.urls')),
    path('timeline/', include('timeline.urls')),
    path('', company_views.home, name='home'),
]
