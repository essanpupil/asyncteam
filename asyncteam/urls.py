from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from asyncteam.views import dashboard, homepage

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/favicon/favicon.ico')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', include('account_profile.urls')),
    path('timeline/', include('timeline.urls')),
    path('project/', include('project_management.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('', homepage, name='homepage'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
