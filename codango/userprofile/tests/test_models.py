from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from userprofile.models import UserProfile


class ProfileTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='adebola', password='adebolu')

    # def create_resources(self, text='some more words', resource_file='resource_file'):
    #     return Resource.objects.create(text=text, author=self.user, resource_file=resource_file)

    def test_for_profile_creation(self):
        # resource = self.create_resources()
        # user = User.objects.create(resource=resource,user=self.user,vote=False)
        self.user = User.objects.create(username='adebola', password='adebolu')
        # self.assertTrue(isinstance(vote, Vote))
        userprofile = UserProfile.objects.get(user_id=self.user.id)
        self.assertTrue(isinstance(userprofile, UserProfile))
