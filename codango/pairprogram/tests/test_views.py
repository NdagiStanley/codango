from django.test.utils import setup_test_environment
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
setup_test_environment()


class PairProgramTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_pair_program_page(self):
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango', body.text)

        # logging in username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Share', body.text)

        # View Sessions page
        self.browser.find_element_by_link_text('Pair Programming').click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Create a new Programming session', body.text)

        # create a new session
        self.browser.find_element_by_link_text(
            'Create a new Programming session').click()
        block = WebDriverWait(self.browser, 60)
        block.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'modal')
            )
        )
        self.browser.find_element_by_name(
            'session_name').send_keys('Pairing Session with the boss')
        self.browser.find_element_by_xpath(
            "//button[contains(text(),'Create')]").click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pairing Session with the boss', body.text)
