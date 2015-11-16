from django.test import TestCase
from resources.models import Resource
from votes.models import Vote
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class VoteTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='inioluwafageyinbo', password='codango')

    def create_resources(self, text='some more words', resource_file='resource_file'):
        return Resource.objects.create(text=text, author=self.user, resource_file=resource_file)

    def test_for_vote_creation(self):
        resource = self.create_resources()
        vote = Vote.objects.create(resource=resource,user=self.user,vote=False)
        self.assertTrue(isinstance(vote, Vote))

    def test_for_vote_is_down_vote(self):
        resource = self.create_resources()
        vote = Vote.objects.create(resource=resource,user=self.user,vote=False)

        self.assertTrue(vote.is_downvote())

    def test_for_vote_is_up_vote(self):
        resource = self.create_resources()
        vote = Vote.objects.create(resource=resource,user=self.user,vote=True)

        self.assertTrue(vote.is_upvote())
