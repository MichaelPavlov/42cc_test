# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.core.urlresolvers import resolve, reverse_lazy
from django.template.loader import render_to_string
from django.test import RequestFactory
from django.test import TestCase

from apps.hello.views import contact_page

User = get_user_model()


class ContactViewTestCase(TestCase):
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
        expected_html = render_to_string("hello/contact.html")
        self.assertEqual(response.content.decode("utf-8"), expected_html)
