from datetime import date

from django.test import RequestFactory
from django.test import TestCase

from apps.hello.models import User, Profile


class RegistrationTestCase(TestCase):
    """
    Base class for registration test cases. Creates User and it's associated profile
    """

    @classmethod
    def setUpClass(cls):
        User.objects.all().delete()
        Profile.objects.all().delete()

        cls.factory = RequestFactory()

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
