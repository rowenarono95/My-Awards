from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.roro = User(username = 'Roro',email = 'rowenarono@gmail.com')
        self.roro = Profile(user = Self.roro,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='dec,01.2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.roro,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.roro.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class ProjectTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',projectscreenshot = 'test.jpg',description = 'testD',user = peris,projecturl = 'https://test.com',datecreated='Dec,01.2020')


    def test_save_project(self):
        self.new_post.save_project()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1)    