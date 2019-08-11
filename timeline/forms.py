from django.forms import ModelForm

from timeline.models import Flow


class FlowForm(ModelForm):
    class Meta:
        model = Flow
        fields = ['name', 'is_master', 'parent']
