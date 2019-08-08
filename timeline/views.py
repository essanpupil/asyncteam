from django.views.generic import edit

from .models import Flow


class MainTimeline(edit.CreateView):
    model = Flow
    fields = ['name']
    template_name = 'timeline/main.html'
