from django.urls import reverse
from django.test import TestCase

from ..views import home

class HomeTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_view_contains_link_to_request_project(self):
        request_project_url = reverse('request_project')
        self.assertContains(self.response, 'href="{0}"'.format(request_project_url))
