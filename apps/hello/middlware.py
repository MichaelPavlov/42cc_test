from apps.hello.models import RequestStamp


class RequestCaptureMiddlware(object):
    def process_request(self, request):
        RequestStamp.objects.create(
            method=request.method,
            path=request.path,
            ip=self.get_ip_address(request)
        )

    def get_ip_address(self, request):
        """ use requestobject to fetch client machine's IP Address """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            # Real IP address of client Machine
            ip = request.META.get('REMOTE_ADDR')
        return ip
