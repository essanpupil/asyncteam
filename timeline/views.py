from django.shortcuts import render


def dashboard(request):
    return render(request, 'timeline/dashboard.html')
