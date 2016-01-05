from django.test import Client, TestCase
import json
from django.contrib.auth.models import User
from resources.models import Resource
from comments.models import Comment
from django.test.utils import setup_test_environment
setup_test_environment()

class CommentActionTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='Abiodun', password='shuaib')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='Abiodun', password='shuaib')

    def create_resources(self, text='some more words', resource_file='resource_file'):
        return Resource.objects.create(id=100, text=text, author=self.user, resource_file=resource_file)

    def test_user_can_post_new_comments(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post('/comment/',
                                    {'content': 'test_content',
                                        'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Successfully')

    def test_user_can_delete_comments(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        comment = Comment(
            id=200, author=self.user, resource=resource, content="Test comment")
        comment.save()
        response = self.client.delete('/comment/200',
                                      HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_user_can_edit_comments(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        comment = Comment(
            id=200, author=self.user, resource=resource, content="Test comment")
        comment.save()
        json_data = json.dumps({'content': 'Another Content', })
        response = self.client.put('/comment/200', json_data, content_type='application/json',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
