from django.conf import settings
from django.shortcuts import render
from django.views.generic import DetailView

from djbusiness.models import Company, Page

BUSINESS_CONFIG = settings.BUSINESS_CONFIG


def home(request):
    company = Company.objects.prefetch_related('page_set', 'contact_set', 'card_set').last()
    company_pages = Page.objects.filter(company=company, display_in_navbar=True)
    context = {
        'company': company,
        'company_pages': company_pages,
        'login_url': BUSINESS_CONFIG['login_url'],
        'register_url': BUSINESS_CONFIG['register_url'],
    }
    return render(request, 'djbusiness/home.html', context)


class PageView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = self.get_object()
        company_pages = Page.objects.filter(company=page.company, display_in_navbar=True)
        context['company'] = page.company
        context['company_pages'] = company_pages
        context['login_url'] = BUSINESS_CONFIG['login_url']
        context['register_url'] = BUSINESS_CONFIG['register_url']
        return context
