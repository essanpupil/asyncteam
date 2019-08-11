from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from djbusiness.models import Company


@login_required
def dashboard(request):
    company = Company.objects.last()
    return render(request, 'dashboard.html', {'company': company})
