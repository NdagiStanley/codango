from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from userprofile.views import UserProfileDetailView, UserProfileEditView, FollowingView, FollowersView


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
                                     'about':'I love to Code'})
        self.assertEqual(response.status_code, 302)


class FollowViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 =User.objects.create_user(username='golden', password='abiodun')
        self.user2 =User.objects.create_user(username='jubril', password='issa')
        self.user1.save()
        self.user2.save()
        self.login = self.client.login(username='golden', password='abiodun')

    def test_can_reach_followers_page(self):
        response = self.client.get('/user/golden/followers')
        self.assertEqual(response.status_code, 200)

    def test_can_reach_following_page(self):
        response = self.client.get('/user/golden/following')
        self.assertEqual(response.status_code, 200)
