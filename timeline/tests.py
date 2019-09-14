import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class DashboardTest(StaticLiveServerTestCase):

    @pytest.mark.skip
    def test_dashboard(self):
        response = self.client.get(self.live_server_url + reverse('dashboard'))
        self.assertEqual(200, response.status_code)
