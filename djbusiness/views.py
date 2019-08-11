from django.shortcuts import render
from django.views.generic import DetailView

from djbusiness.models import Company, Page


def home(request):
    company = Company.objects.prefetch_related('page_set', 'contact_set', 'card_set').last()
    company_pages = Page.objects.filter(company=company, display_in_navbar=True)
    return render(request, 'djbusiness/home.html', {'company': company, 'company_pages': company_pages})


class PageView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = self.get_object()
        company_pages = Page.objects.filter(company=page.company, display_in_navbar=True)
        context['company'] = page.company
        context['company_pages'] = company_pages
        return context
