from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/timeline/favicon/favicon.ico')),
    path('timeline/', include('timeline.urls')),
]
