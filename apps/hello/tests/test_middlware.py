from apps.hello.middlware import RequestCaptureMiddlware
from django.test import RequestFactory
from django.test import TestCase

from apps.hello.models import RequestStamp


class RequestCaptureMiddlwareTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = RequestFactory()
        cls.rc_middlware = RequestCaptureMiddlware()

    def test_basic_capture_request(self):
        """
        Test that RequestCaptureMiddlware captures requests to RequestStamp model
        """
        url = "/"
        request = self.factory.get(url)
        models_before = RequestStamp.objects.count()
        self.rc_middlware.process_request(request)
        models_after = RequestStamp.objects.count()

        self.assertNotEqual(models_after, models_before)
