from django.test import TestCase
from django.utils import timezone
from clan_pages.models import Clan
from .models import Match
from django.contrib.auth.models import User


class matchTestCase(TestCase):

    def setUp(self):
        # Create instances of Clan to use in tests
        self.user = User.objects.create_user(username="test1",
                                             email="test@test.com",
                                             password="test123")
        self.user2 = User.objects.create_user(username="test2",
                                              email="test@test2.com",
                                              password="test122")
        self.clan1 = Clan.objects.create(user=self.user)
        self.clan2 = Clan.objects.create(user=self.user2)

    def test_match_creation(self):
        # Create a match instance
        match = Match.objects.create(
            inviter_clan=self.clan1,
            invitee_clan=self.clan2,
            game_type="18vs18",
            match_date=timezone.now(),
            message="Test match",
            is_accepted="in-progress"
        )
        # Check that the match instance is created successfully
        self.assertEqual(match.inviter_clan, self.clan1)
        self.assertEqual(match.invitee_clan, self.clan2)
        self.assertEqual(match.game_type, "18vs18")
        self.assertEqual(match.message, "Test match")
        self.assertEqual(match.is_accepted, "in-progress")

    def test_game_type_choices(self):
        match = Match.objects.create(
            inviter_clan=self.clan1,
            invitee_clan=self.clan2,
            game_type="18vs18",
            match_date=timezone.now(),
            message="Test match",
            is_accepted="in-progress"
        )
        choices = [
            choice[0]
            for choice in Match._meta.get_field('game_type').choices
        ]
        self.assertIn(match.game_type, choices)

    def test_is_accepted_default_value(self):
        match = Match.objects.create(
            inviter_clan=self.clan1,
            invitee_clan=self.clan2,
            game_type="18vs18",
            match_date=timezone.now(),
            message="Test match"
        )
        self.assertEqual(match.is_accepted, "in-progress")
