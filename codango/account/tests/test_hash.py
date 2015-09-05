from django.test import TestCase, Client
from django.contrib.auth.models import User
from account.hash import UserHasher

class HashTest(TestCase):
    """ This class tests the user account hash generation and hash reversing functions defined in the 'account.hashs'module.
        It tests the round trip: generating a unique hash for a user and then testing it against results of the reverse process"""
    
    def setUp(self):
        # create a test client:
        self.client = Client()
        # register a sample user:
        self.registered_account = User.objects.create_user('OlufunmiladeGit', 'Olufunmilade.Git@andela.com', 'ladegit')
        self.registered_account.first_name = 'Olufunmilade'
        self.registered_account.last_name = 'Git'
        self.registered_account.save()


    def test_gen_hash_returns_min_15_chars(self):
        generated_hash = UserHasher.gen_hash(self.registered_account)
        self.assertGreaterEqual(len(generated_hash), 15)


    def test_reverse_hash_returns_user_instance(self):
        generated_hash = UserHasher.gen_hash(self.registered_account)
        reversed_hash_result = UserHasher.reverse_hash(generated_hash)
        self.assertIsInstance(reversed_hash_result, User)


    def test_reverse_hash_returns_None_for_Wrong_hash(self):
        generated_hash = "a2374920910"
        reversed_hash_result = UserHasher.reverse_hash(generated_hash)
        self.assertEquals(reversed_hash_result, None)


    def test_generated_hash_reverses_correctly(self):
        generated_hash = UserHasher.gen_hash(self.registered_account)
        reversed_hash_result = UserHasher.reverse_hash(generated_hash)
        self.assertEquals(self.registered_account.pk, reversed_hash_result.pk)