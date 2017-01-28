from apps.hello.models import RequestStamp


class RequestCaptureMiddlware(object):
    def process_request(self, request):
        RequestStamp.objects.create()
