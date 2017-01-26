from datetime import date

from django.contrib.auth import get_user_model
from django.core.urlresolvers import resolve, reverse_lazy
from django.test import RequestFactory
from django.test import TestCase

from apps.hello.models import Profile
from apps.hello.views import contact_page

User = get_user_model()


class ContactViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ContactViewTestCase, cls).setUpClass()

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

    def setUp(self):
        self.factory = RequestFactory()

    def test_resolve_url_for_contact_page(self):
        """
        Test that contact page resolves by right url
        """
        resolver = resolve('/')
        self.assertEqual(resolver.func, contact_page)

    def test_contact_view_basic(self):
        """
        Test that contact view returns a 200 response and uses correct template
        """
        url = reverse_lazy("contact")
        request = self.factory.get(url)
        with self.assertTemplateUsed('hello/contact.html'):
            response = contact_page(request)
            self.assertEqual(response.status_code, 200)

    def test_contact_page_returns_correct_html(self):
        """
        Test for correct data in response of contact_page view
        """
        url = reverse_lazy("contact")
        request = self.factory.get(url)
        response = contact_page(request)
        self.assertIn(b'<p><strong>Name:</strong> Michael</p>',
                      response.content)
        self.assertIn(b'<p><strong>Last name:</strong> Pavlov</p>',
                      response.content)
        self.assertIn(b'<p><strong>Email:</strong> mihpavlov@gmail.com</p>',
                      response.content)
        self.assertIn(b'<p><strong>Jabber:</strong> mirak@xmpp.pro</p>',
                      response.content)
