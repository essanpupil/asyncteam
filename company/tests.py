from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class HomepageTest(StaticLiveServerTestCase):
    def test_homepage(self):
        response = self.client.get(self.live_server_url)
        self.assertEqual(200, response.status_code)

