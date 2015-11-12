from django.test import TestCase
from resources.models import Resource
from django.contrib.auth.models import User
from mock import patch


class ResourceTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='inioluwafageyinbo', password='codango')
        self.resource = Resource.objects.create(
            text='test file',
            author=self.user
        )

    def test_for_resource_creation(self):
        self.assertTrue(Resource.objects.all())

    def test_file_save(self):
        with patch.object(Resource.resource_file.field, 'pre_save', return_value='test.pdf') as mock_method:
            uploadlink = mock_method('test.pdf')
            self.resource.resource_file = uploadlink
            self.resource.save()
            publicid = Resource.objects.filter(
                resource_file=uploadlink)[0].resource_file.public_id
            self.assertEqual(publicid, 'test')
