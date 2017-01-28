from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.hello.models import Profile

User = get_user_model()


class ProfileModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ProfileModelTestCase, cls).setUpClass()

        User.objects.all().delete()
        Profile.objects.all().delete()

        cls.user = User.objects.create(
            username='mirak',
            email="mihpavlov@gmail.com",
            first_name="Michael",
            last_name="Pavlov",

        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            bio="Brief bio...",
            birth_date=date(1984, 10, 12),
            jabber='mirak@xmpp.pro',
            skype='mihpavlov',
        )

    def test_profile_basic(self):
        """
        Test basic functionality of Profile model
        """
        self.assertEqual(self.profile.user.first_name, "Michael")
        self.assertEqual(self.profile.user.email, "mihpavlov@gmail.com")
        self.assertEqual(self.profile.birth_date, date(1984, 10, 12))
        self.assertEqual(self.profile.jabber, "mirak@xmpp.pro")
