from django.views.generic import CreateView, ListView

from project_management.models import Project


class NewProject(CreateView):
    model = Project


class ProjectList(ListView):
    model = Project
