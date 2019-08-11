from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from company.models import Business, Page


class IntegrationTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        ff_options = Options()
        ff_options.headless = True
        self.browser = webdriver.Firefox(options=ff_options)

    def tearDown(self) -> None:
        self.browser.close()

    def create_business(self) -> Business:
        business = Business(name="AsyncTeam")
        business.save()
        self.business = business
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
        self.page = page
        return page

    def create_user(self, username='john', password='doe'):
        user = get_user_model().objects.create(
            username=username,
            is_active=True)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        self.user = user
        return user

    def logging_in_user(self, user, user_password) -> None:
        self.create_business()
        self.browser.get(self.live_server_url)
        signin_nav = self.browser.find_element_by_link_text('Sign In')
        signin_nav.click()
        self.assertEqual(self.browser.title, 'Sign In to AsyncTeam')

        username_input = self.browser.find_element_by_id('id_login')
        username_input.send_keys(user.username)

        password_input = self.browser.find_element_by_id('id_password')
        password_input.send_keys(user_password)

        signin_button = self.browser.find_element_by_class_name('primaryAction')
        signin_button.click()
