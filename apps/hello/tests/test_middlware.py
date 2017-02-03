from django.test import RequestFactory
from django.test import TestCase

from apps.hello.middlware import RequestCaptureMiddlware
from apps.hello.models import RequestStamp


class RequestCaptureMiddlwareTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = RequestFactory()
        cls.rc_middlware = RequestCaptureMiddlware()

    def test_basic_capture_request(self):
        """
        Test that RequestCaptureMiddlware captures requests to
        RequestStamp model
        """
        url = "/"
        request = self.factory.get(url)
        models_before = RequestStamp.objects.count()
        self.rc_middlware.process_request(request)
        models_after = RequestStamp.objects.count()

        self.assertNotEqual(models_after, models_before)

    def test_middlware_with_client(self):
        """
        Test that request sent with client capturing to RequestStamp model
        """
        url = "/random/page/for/testing/with/client/"
        self.client.put(url)
        latest_request_stamp = RequestStamp.objects.latest('id')
        self.assertEqual(latest_request_stamp.method, "PUT")

    def test_middlware_does_not_save_ajax_requests(self):
        """
        Test that middlware does not save ajax requests
        """
        url = "/random/page/for/testing/with/client/"
        models_before = RequestStamp.objects.count()
        self.client.get(url, **{
            'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        models_after = RequestStamp.objects.count()
        self.assertEqual(models_after, models_before)
