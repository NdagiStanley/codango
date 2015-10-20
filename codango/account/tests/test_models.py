from django.test import TestCase
from account.models import UserProfile
from django.contrib.auth.models import User


class UserProfileTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='jubril', password='awesome')

    def test_user_profile_creation(self):
        self.assertEqual(self.user.get_username(), "jubril")
