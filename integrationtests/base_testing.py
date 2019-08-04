from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from company.models import Business, Page


class IntegrationTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        ff_options = Options()
        ff_options.headless = False
        self.browser = webdriver.Firefox(options=ff_options)

    def tearDown(self) -> None:
        self.browser.close()

    def create_business(self) -> Business:
        business = Business(name="AsyncTeam")
        business.save()
        return business

    def create_nav_page(self, business) -> Page:
        page = Page(
            business=business,
            name="About Us",
            slug="about-us",
            display_in_navbar=True,
            html_code="We are fighting dreamer",
        )
        page.save()
        return page

