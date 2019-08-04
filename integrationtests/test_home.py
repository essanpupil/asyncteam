import pytest

from integrationtests.base_testing import IntegrationTest


class HomepageTest(IntegrationTest):

    @pytest.mark.django_db(transaction=True)
    def test_home(self):
        business = self.create_business()
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.title, "Welcome to {}".format(business.name))
