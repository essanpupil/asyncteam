from django.urls import path

from project_management.views import NewProject, ProjectList

app_name = 'project_management'
urlpatterns = [
    path('new',  NewProject.as_view(), name='new_project'),
    path('', ProjectList.as_view(), name='project_dashboard'),
]
