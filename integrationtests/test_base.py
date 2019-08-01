from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class IntegrationTest(StaticLiveServerTestCase):

    def test_something(self):
        ff_options = Options()
        ff_options.headless = True
        browser = webdriver.Firefox(options=ff_options)
        browser.get(self.live_server_url)
        self.assertEqual(browser.title, "Welcome to AsyncTeam")
