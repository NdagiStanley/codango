from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.models import UserProfile


class ProfileTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='adebola', password='adebolu')

    def test_for_profile_creation(self):

        userprofile = UserProfile.objects.get(user_id=self.user.id)
        self.assertTrue(isinstance(userprofile, UserProfile))
