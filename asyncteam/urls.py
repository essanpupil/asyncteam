from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from asyncteam.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', include('account_profile.urls')),
    path('timeline/', include('timeline.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('', include('djbusiness.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
