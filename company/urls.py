from django.urls import path

from company import views


app_name = 'company'
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.PageView.as_view(), name='page')
]