# -*- coding: utf-8 -*-
from datetime import date

from django.contrib.auth import get_user_model
from django.core import serializers
from django.core.urlresolvers import resolve, reverse_lazy
from django.template.loader import render_to_string
from django.test import RequestFactory
from django.test import TestCase

from apps.hello.models import Profile, RequestStamp
from apps.hello.views import contact_page, request_stamps_view

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

        cls.factory = RequestFactory()

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
        context = {'profile': self.profile}
        expected_html = render_to_string("hello/contact.html",
                                         dictionary=context)
        self.assertEqual(response.content.decode("utf-8"), expected_html)


class RequestStampsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(RequestStampsViewTestCase, cls).setUpClass()

        RequestStamp.objects.all().delete()

        cls.request_stamps = [
            {
                "id": 1,
                "method": "PATCH",
                "path": "/test/path/url/1/",
                "ip": "192.168.0.1",
                "new": False
            },
            {
                "id": 2,
                "method": "GET",
                "path": "/test/path/url/2/",
                "ip": "192.168.0.2",
                "new": True
            },
            {
                "id": 3,
                "method": "POST",
                "path": "/test/path/url/3/",
                "ip": "192.168.0.3",
                "new": True
            },
        ]

        RequestStamp.objects.bulk_create(
            [RequestStamp(**vals) for vals in cls.request_stamps]
        )

        cls.factory = RequestFactory()

    def test_resolve_url_for_request_stamp_view(self):
        """
        Test that request stamp view resolves by right url
        """
        resolver = resolve("/api/request_stamps/")
        self.assertEqual(resolver.func, request_stamps_view)

    def test_request_stamps_view_basic(self):
        """
        Test that request stamps view returns a 200 response
        """
        url = reverse_lazy("request-stamps")
        request = self.factory.get(url)

        response = request_stamps_view(request)
        self.assertEqual(response.status_code, 200)

    def test_request_stamp_url_returns_correct_data(self):
        """
        Test that client can get correct data accessing stamp url
        """
        qs = RequestStamp.objects.filter(new=True)
        json = serializers.serialize("json", qs)

        url = reverse_lazy("request-stamps")
        response = self.client.get(url)
        self.assertEqual(response, json)
