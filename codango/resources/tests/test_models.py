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
            author=self.user,
            resource_file='help'
        )

    def test_for_resource_creation(self):
        self.assertTrue(Resource.objects.all())

    # mock cloudinary pre_save function that returns a public_id for uploads
    def test_file_save(self):
        with patch.object(Resource.resource_file.field, 'pre_save', return_value='test.pdf') as mock_method:
            uploadlink = mock_method('test.pdf')
            self.resource.resource_file = uploadlink
            self.resource.save()
            resourcefile = Resource.objects.filter(
                resource_file=uploadlink)[0].resource_file
            publicid = resourcefile.public_id
            cloudinaryurl = resourcefile.url
            fileformat = resourcefile.format
            self.assertEqual(publicid, 'test')
            self.assertEqual(
                cloudinaryurl,
                'http://res.cloudinary.com/codangofile/image/upload/test.pdf')
            self.assertEquals(fileformat, 'pdf')
