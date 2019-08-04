import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class IntegrationTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        ff_options = Options()
        ff_options.headless = False
        self.browser = webdriver.Firefox(options=ff_options)
        self.browser.get(self.live_server_url)

    def tearDown(self) -> None:
        self.browser.close()

    @pytest.mark.django_db(transaction=True)
    def test_something(self):
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.title, "Welcome to AsyncTeam")
