from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import edit, list

from timeline.forms import FlowForm
from .models import Flow


class MainTimeline(list.ListView):
    model = Flow
    fields = ['name']
    template_name = 'timeline/main.html'


class NewTimeline(edit.CreateView):
    model = Flow
    form_class = FlowForm
    template_name = 'timeline/new.html'

    def post(self, request, *args, **kwargs):
        flow_form = self.get_form()
        if flow_form.is_valid():
            new_flow = flow_form.save(commit=False)
            new_flow.owner = self.request.user
            new_flow.save()
            return redirect(reverse('timeline:main'))
        else:
            return flow_form.invalis()
