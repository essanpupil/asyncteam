from django.urls import path

from account_profile import views

app_name = 'account_profile'
urlpatterns = [
    path('<slug:username>', views.UserProfile.as_view(), name='detail'),
    path('', views.CurrentUserProfile.as_view(), name='current_user'),
]
