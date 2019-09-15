import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from project_management.models import Project


class NewProjectTestCase(TestCase):

    @pytest.mark.skip
    def test_new_project(self):
        user = User.objects.create_user('johndoe', 'rasalemon')
        client = Client()
        client.login(username='johndoe', password='rasalemon')
        response = client.post(
            reverse('project_management:new_project'),
            {
                'name': 'First Test Project',
                'description': 'This is my first project for the app',
                'creator': user.id,
                'member': (user.id,),
            },
            follow=True
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Project.objects.all()), msg=response.get_raw_uri())
