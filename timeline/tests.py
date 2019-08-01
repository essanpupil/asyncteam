from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class HomepageTest(StaticLiveServerTestCase):
    def test_homepage(self):
        response = self.client.get(self.live_server_url)
        self.assertEqual(200, response.status_code)


class DashboardTest(StaticLiveServerTestCase):
    def test_dashboard(self):
        response = self.client.get(self.live_server_url + reverse('timeline:dashboard'))
        self.assertEqual(200, response.status_code)
