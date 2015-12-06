from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.models import UserProfile, Language


class ProfileTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='adebola', password='adebolu')
        self.language = Language.objects.create(name="Python", user=self.user)

    def test_for_profile_creation(self):

        userprofile = UserProfile.objects.get(user_id=self.user.id)
        self.assertTrue(isinstance(userprofile, UserProfile))

    def test_for_language(self):
        language = str(self.language)
        self.assertIsNotNone(language)
