from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CodangoTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        # functional testing done in firefox browser
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_and_login_admin_site(self):
        # open web browser and go to admin page
        self.browser.get(self.live_server_url + '/admin/')

        # site heading should be 'Django administration'
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # testing username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # more tests needed
