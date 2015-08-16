from django.test import LiveServerTestCase
from selenium import webdriver

class PollsTest(LiveServerTestCase):

	def setUp(self):
		# functional testing done in firefox browser
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_poll_via_admin_site(self):
		# open web browser and go to admin page
		self.browser.get(self.live_server_url + '/admin/')

		# site heading should be 'Django administration'
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		# more tests needed
