import pytest

from integrationtests.base_testing import IntegrationTest


class PageDetailTest(IntegrationTest):

    @pytest.mark.django_db(transaction=True)
    def test_go_to_page_from_home(self):
        business = self.create_business()
        page = self.create_nav_page(business)
        self.browser.get(self.live_server_url)
        nav_links = self.browser.find_elements_by_class_name('nav-link')
        nav_links[0].click()
        self.assertEqual(self.browser.title, page.name)
