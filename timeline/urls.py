from django.urls import path

from timeline import views

app_name = 'timeline'
urlpatterns = [
    path('', views.MainTimeline.as_view(), name='main'),
    path('new', views.NewTimeline.as_view(), name='new'),
    path('delete/<int:pk>', views.DeleteTimeline.as_view(), name='delete'),
]
