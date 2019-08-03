from django.shortcuts import render
from django.views.generic import DetailView

from company.models import Business, Page


def home(request):
    business = Business.objects.first()
    return render(request, 'company/home.html', {'business': business})


class PageView(DetailView):
    model = Page
