from integrationtests.base_testing import IntegrationTest


class LoginTest(IntegrationTest):
    def test_login(self):
        self.create_business()
        self.create_user('jojo', 'badminton')
        self.browser.get(self.live_server_url)
        signin_nav = self.browser.find_element_by_link_text('Sign In')
        signin_nav.click()
        self.assertEqual(self.browser.title, 'Sign In to AsyncTeam')

        username_input = self.browser.find_element_by_id('id_login')
        username_input.send_keys('jojo')

        password_input = self.browser.find_element_by_id('id_password')
        password_input.send_keys('badminton')

        signin_button = self.browser.find_element_by_class_name('primaryAction')
        signin_button.click()

        self.assertEqual("Hello jojo", self.browser.title)
