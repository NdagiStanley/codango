from django.test import TestCase
from resources.models import Resource
from votes.models import Vote
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

    def create_resources(self, text='some more words', resource_file='resource_file'):
        return Resource.objects.create(text=text, author=self.user, resource_file=resource_file)
        
    def test_for_resource_creation(self):
        self.assertIsNotNone(Resource.objects.all())



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
        create = self.create_resources()
        self.assertTrue(isinstance(create, Resource))

    def test_for_upvote(self):
    	resource = self.create_resources()
        vote = Vote()
    	vote.user = self.user
    	vote.resource = resource
    	vote.vote = True
    	vote.save()
    	self.assertEqual(len(resource.upvotes()),1)
        
    def test_for_downvote(self):
    	resource = self.create_resources()
        vote = Vote()
    	vote.user = self.user
    	vote.resource = resource
    	vote.vote = False
    	vote.save()
    	self.assertEqual(len(resource.downvotes()),1)

