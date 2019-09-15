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
