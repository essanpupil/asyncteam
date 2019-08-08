from django.urls import path

from timeline import views

app_name = 'timeline'
urlpatterns = [
    path('', views.MainTimeline.as_view(), name='main')
]