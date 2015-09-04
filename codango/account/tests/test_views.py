from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import TestCase

class IndexViewTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_index_page_and_log_in(self):
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango', body.text)

        # testing username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango Home', body.text)
