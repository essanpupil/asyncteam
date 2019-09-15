from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class IntegrationTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        ff_options = Options()
        ff_options.headless = True
        self.browser = webdriver.Firefox(options=ff_options)

    def tearDown(self) -> None:
        self.browser.close()

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
        self.browser.get(self.live_server_url)
        signin_nav = self.browser.find_element_by_link_text('Login')
        signin_nav.click()
        self.assertEqual('Login to AsyncTeam', self.browser.title)

        username_input = self.browser.find_element_by_id('id_login')
        username_input.send_keys(user.username)

        password_input = self.browser.find_element_by_id('id_password')
        password_input.send_keys(user_password)

        signin_button = self.browser.find_element_by_id('IdLogin')
        signin_button.click()
