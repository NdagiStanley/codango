from django.test import TestCase
from resources.models import Resource
from comments.models import Comment
from django.contrib.auth.models import User


class CommentTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='inioluwafageyinbo', password='codango')

    def create_resources(
            self, text='some more words',
            resource_file='resource_file'):
        return Resource.objects.create(
            text=text,
            author=self.user,
            resource_file=resource_file
        )

    def test_for_comment_creation(self):
        resource = self.create_resources()
        comment = Comment.objects.create(
            resource=resource,
            author=self.user,
            content="This is a test comment"
        )
        self.assertTrue(isinstance(comment, Comment))

    def test_for_comment_str_content(self):
        resource = self.create_resources()
        comment = Comment.objects.create(
            resource=resource,
            author=self.user,
            content="This is a test comment"
        )
        content = str(comment)
        self.assertIsNotNone(content)
