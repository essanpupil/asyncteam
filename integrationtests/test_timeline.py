from integrationtests.base_testing import IntegrationTest


class TimelineTest(IntegrationTest):
    def go_to_timeline_dashboard(self):
        self.create_business()
        self.create_user('jojo', 'badminton')
        self.logging_in_user(self.user, 'badminton')

        timeline_nav = self.browser.find_element_by_link_text('Timeline')
        timeline_nav.click()

    def test_go_to_timeline_dashboard(self):
        self.create_business()
        self.create_user('jojo', 'badminton')
        self.logging_in_user(self.user, 'badminton')

        timeline_nav = self.browser.find_element_by_link_text('Timeline')
        timeline_nav.click()
        self.assertEqual(self.browser.title, 'Timeline Dashboard')

    def test_create_main_timeline(self):
        self.go_to_timeline_dashboard()
        create_timeline_menu = self.browser.find_element_by_id('create-main-timeline')
        create_timeline_menu.click()
        self.assertEqual("Create main timeline", self.browser.title)
