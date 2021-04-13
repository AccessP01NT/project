from django.test import TestCase
from login import views

class Agile_testCase(TestCase):
    def test_isName(self):
        res =views.isName("to2m2er")
        self.assertTrue(res)
    def test_isRole(self):
        res =views.isRole("teammate")
        self.assertTrue(res)
    def test_isUserName(self):
        res =views.isUserName("2UserName")
        self.assertTrue(res)
# Create your tests here.
