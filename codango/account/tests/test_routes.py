from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from account.views import ForgotPasswordView, ResetPasswordView
from mock import patch
from account.emails import SendGrid
from resources.models import Resource
from pairprogram.models import Session, Participant


class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username='lade',
            password='password',
        )
        self.initiator = User.objects.create_user(
                username='andela',
                password='awesome',
                email='andela@andela.com'
        )
        self.pair_session = Session.objects.create(
            initiator=self.initiator, session_name="SomeRandomSession")

    def test_can_reach_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_right_view_for_index_is_returned(self):
        match = resolve('/')
        self.assertEqual(match.url_name, 'index')

    def test_can_login(self):
        response = self.client.post('/login', {
            'username': 'lade',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)

    def test_can_register(self):
        response = self.client.post('/register', {
            'username': 'lade.o',
            'password': 'password',
            'password_conf': 'password',
            'email': 'olufunmilade.oshodi@andela.com'
        })
        self.assertEqual(response.status_code, 302)

    def test_can_register_and_create_session(self):
        response = self.client.post('/register', {
            'username': 'lade.o',
            'password': 'password',
            'password_conf': 'password',
            'session_id': 1,
            'email': 'olufunmilade.oshodi@andela.com'
        })
        session_program = Participant.objects.all()
        self.assertEqual(len(session_program), 1)
        self.assertEqual(response.status_code, 302)


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='lade',
            password='password'
        )
        self.user.set_password('password')
        self.user.save()
        self.login = self.client.login(
            username='lade', password='password')

    def test_can_reach_home_page(self):
        self.assertEqual(self.login, True)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_right_view_for_home_is_returned(self):
        match = resolve('/home')
        self.assertEqual(match.url_name, 'home')


class SearchViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='lade',
            password='password'
        )
        self.user.set_password('password')
        self.user.save()
        self.login = self.client.login(
            username='lade', password='password')

    def create_resources(self, text='some more words',
                         resource_file='resource_file'):
        return Resource.objects.create(
            text=text, author=self.user, resource_file=resource_file
        )

    def test_can_reach_search_page(self):
        self.assertEqual(self.login, True)
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    def test_can_search_based_on_user_or_resource(self):
        self.create_resources()
        self.create_resources()
        url = reverse('search_by', kwargs={'searchby': 'resources'})
        url2 = reverse('search_by', kwargs={'searchby': 'users'})

        response = self.client.get(url)
        response2 = self.client.get(url2)

        self.assertEqual(len(response.context['resources']), 2)
        self.assertEqual(len(response.context['users']), 1)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response.status_code, 200)

    def test_return_no_user_or_response_when_not_resource_is_found(self):
        self.create_resources()
        self.create_resources()
        url = reverse('search_by', kwargs={'searchby': 'resources'})
        url2 = reverse('search_by', kwargs={'searchby': 'users'})

        response = self.client.get(url + "?q=eaiofaowfjieaowef")
        response2 = self.client.get(url2 + "?q=eaiofaowfjieaowef")

        self.assertEqual(len(response.context['resources']), 0)
        self.assertEqual(len(response.context['users']), 0)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response.status_code, 200)


class ForgotResetTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_forgot_route_resolves_to_correct_view(self):
        response = self.client.get('/recovery')
        self.assertEqual(
            response.resolver_match.func.__name__,
            ForgotPasswordView.as_view().__name__)

    def test_reset_route_resolves_to_correct_view(self):
        response = self.client.get(
            '/recovery/ajkzfYba9847DgJ7wbkwAaSbkTjUdawGG998qo3HG8qae83')
        self.assertEqual(
            response.resolver_match.func.__name__,
            ResetPasswordView.as_view().__name__)


class PasswordResetTestCase(TestCase):

    def setUp(self):
        # create a test client:
        self.client = Client()
        # register a sample user:
        self.user_account = User.objects.create_user(
            'inioluwafageyinbo', 'inioluwafageyinbo@gmail.com', 'codango')
        self.user_account.first_name = 'Inioluwa'
        self.user_account.last_name = 'Fageyinbo'
        self.user_account.save()

    def test_get_returns_200(self):
        response = self.client.get('/recovery')
        self.assertEquals(response.status_code, 200)

    def test_recovery_email_not_sent_for_unregistered_user(self):
        response = self.client.post(
            '/recovery', {"email": "fagemaki.iniruto@gmail.com"})
        self.assertNotIn('email_status', response.context)


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='lade',
            password='password'
        )
        self.user.set_password('password')
        self.user.save()
        self.login = self.client.login(
            username='lade', password='password')

    def test_can_reach_profile_page(self):
        response = self.client.get('/user/lade')
        self.assertEqual(response.status_code, 200)

    def test_can_reach_profile_edit_page(self):
        response = self.client.post('/user/lade/edit',
                                    {'position': 'Software Developer',
                                     'place_of_work': 'Andela',
                                     'first_name': 'Lade',
                                     'last_name': 'Oshodi',
                                     'about': 'I love to Code'})
        self.assertEqual(response.status_code, 302)


class ContactUsViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_can_reach_contact_us_page(self):
        response = self.client.get(reverse('contactus'))
        self.assertEqual(response.status_code, 200)

    def test_right_template_for_contact_us_page_is_returned(self):
        response = self.client.get(reverse('contactus'))
        self.assertEqual(response.templates[0].name, 'account/contact-us.html')

    @patch.object(SendGrid, 'send')
    def test_send_message(self, mock_method):
        response = self.client.post('/contact-us', {
            'name': 'Test User',
            'email': 'test.user@test.com',
            'subject': 'Test',
            'message': 'This is a test message'
        })
        self.assertEqual(response.status_code, 302)


class AboutUsViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_can_reach_about_us_page(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_right_template_for_about_us_page_is_returned(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.templates[0].name, 'account/about-us.html')


class TeamViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_can_reach_team_page(self):
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, 200)

    def test_right_template_for_team_page_is_returned(self):
        response = self.client.get(reverse('team'))
        self.assertEqual(response.templates[0].name, 'account/team.html')
