from django.shortcuts import render
from django.views.generic import DetailView

from company.models import Business, Page


def home(request):
    business = Business.objects.last()
    business_pages = Page.objects.filter(business=business, display_in_navbar=True)
    return render(request, 'company/home.html', {'business': business, 'business_pages': business_pages})


class PageView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = self.get_object()
        business_pages = Page.objects.filter(business=page.business, display_in_navbar=True)
        context['business'] = page.business
        context['business_pages'] = business_pages
        return context
