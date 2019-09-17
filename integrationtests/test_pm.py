from selenium.webdriver.support.select import Select

from integrationtests.base_testing import IntegrationTest


class NewProjectTestCase(IntegrationTest):
    def test_new_project(self):
        user = self.create_user("cessar", "rajayunani")
        self.logging_in_user(user, "rajayunani")

        project_menu = self.browser.find_element_by_id('tasksDropdown')
        project_menu.click()

        new_project_menu = self.browser.find_element_by_link_text('New Project')
        new_project_menu.click()
        self.assertEqual('New Project', self.browser.title)

        self.browser.find_element_by_id('id_name').send_keys("Test Project One")
        self.browser.find_element_by_id('id_description').send_keys('This is a test project. I want this project to be displayed in project list')
        Select(self.browser.find_element_by_id('id_creator')).select_by_visible_text("cessar")
        Select(self.browser.find_element_by_id('id_member')).select_by_visible_text("cessar")
        self.browser.find_element_by_id('saveProject').click()

        self.assertEqual('All Project', self.browser.title)
