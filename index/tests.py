from django.test import TestCase, Client
from clan_pages.models import Clan
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.
class indexTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # test user
        self.user = User.objects.create_user(username="test1",
                                             email="test@test.com",
                                             password="test123")

        # dummy clans
        Clan.objects.create(
            user=self.user,
            clan_name="test-clan-1",
            content="Content for clan 1",
            discord_url="http://discord1.com"
        )
        Clan.objects.create(
            user=self.user,
            clan_name="test-clan-2",
            content="Content for clan 2",
            discord_url="http://discord2.com"
        )
        Clan.objects.create(
            user=self.user,
            clan_name="test-clan-3",
            content="Content for clan 3",
            discord_url="http://discord3.com"
        )

    def test_index_page_view(self):
        """Test the index page view loads correctly with clan pages"""
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # Check the index page to make sure correct clans passed
        clans = response.context['clans']
        self.assertEqual(len(clans), 3)
        self.assertEqual(clans[0].clan_name, "test-clan-1")
        self.assertEqual(clans[1].clan_name, "test-clan-2")
        self.assertEqual(clans[2].clan_name, "test-clan-3")

    def test_error_view(self):
        """Test that the error_view is triggered for a 404 error."""
        # Make a GET request to a non-existent URL
        response = self.client.get('incorrect-url/')

        # checks that the page is not found and a 404 error code is returned
        self.assertEqual(response.status_code, 404)

        # checks that the 404.html is displayed due to incorrect url
        self.assertTemplateUsed(response, '404.html')
