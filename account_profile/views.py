from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'


class CurrentUserProfile(LoginRequiredMixin, DetailView):
    model = User

    def get_object(self, queryset=None):
        user = User.objects.get(id=self.request.user.id)
        return user
