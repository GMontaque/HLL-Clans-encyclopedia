from django.test import TestCase, Client
from .models import Clan
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.
class clanTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="test1", email="test@test.com")
        user.set_password("test123")
        user.save()

        clan = Clan.objects.create(
            user=user,
            clan_name="test-clan",
            content="ffsdfgsfsdfsdfds",
            discord_url="afafagag"
        )
        clan.save()
        self.client = Client()

    def test_model_creation(self):
        # test for model
        clan = Clan.objects.get(clan_name="test-clan")
        self.assertEqual(clan.clan_name, "test-clan")

    def test_clan_creation_view(self):
        # clan creation view
        self.client.login(username="test1", password="test123")
        data = {
            "clan_name": "test-clan",
            "content": "ffsdfgsfsdfsdfds",
            "discord_url": "afafagag"
        }
        response = self.client.post(reverse("clan_creation"), data)
        self.assertEqual(response.status_code, 302)

    def test_clan_page_view(self):
        # clan page view
        self.client.login(username="test1", password="test123")
        clan_name = "test-clan"
        url = reverse("clan_page", kwargs={"clan_name": clan_name})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_clan_page_view_get(self):
        # edit clan page - GET
        self.client.login(username="test1", password="test123")
        clan_name = "test-clan"
        url = reverse("edit_clan_page", kwargs={"clan_name": clan_name})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_clan_page_view_post(self):
        # edit clan page - POST
        data = {
            "clan_name": "test-clan-update",
            "content": "ffsdfgsfsdfsdfds-update",
            "discord_url": "afafagag-update"
        }
        clan_name = "test-clan"
        url = reverse("edit_clan_page", kwargs={"clan_name": clan_name})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_delete_clan_view(self):
        self.client.login(username="test1", password="test123")
        clan_name = "test-clan"
        url = reverse("delete_clan", kwargs={"clan_name": clan_name})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
