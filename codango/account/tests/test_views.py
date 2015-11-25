from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class IndexViewTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_index_page_and_log_in_and_logout(self):
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

        # logging out
        self.browser.find_element_by_link_text('lade').click()
        self.browser.find_element_by_link_text('LogOut').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Join Our Community', body.text)


class UserProfileTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_profile_page(self):
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

        # User profile
        self.browser.find_element_by_link_text('lade').click()
        self.browser.find_element_by_link_text('View Profile').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('@lade', body.text)


class CreateResource(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_resource(self):
        self.browser.get(self.live_server_url)

        # logging in username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        # creating a resource
        input_field = self.browser.find_element_by_id('id-plain-text')
        input_field.send_keys('This is a post')
        self.browser.find_element_by_xpath(
            "//button[contains(text(),'Share')]").click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('success', body.text)


class StaticPages(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_static_pages(self):
        self.browser.get(self.live_server_url)

        # index page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Join Our Community', body.text)

        # about us page
        self.browser.find_element_by_link_text('About Us').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('About us', body.text)

        # contact us page
        self.browser.find_element_by_link_text('Contact Us').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Contact us', body.text)

        # team page
        self.browser.find_element_by_link_text('Team').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Our Awesome Team', body.text)
