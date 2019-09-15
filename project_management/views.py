from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from project_management.models import Project


class NewProject(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_management:project_dashboard')


class ProjectList(LoginRequiredMixin, ListView):
    model = Project
