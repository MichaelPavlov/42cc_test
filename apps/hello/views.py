from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render

from apps.hello.models import Profile, RequestStamp


def contact_page(request):
    """
    Implements contact view.
    :param request:
    :return:
    """

    # Here we get first object as it would be the only one in database, since
    # this is a demo project. If there were listing we would implement
    # filtering with request parameter

    profile = Profile.objects.get(pk=1)
    context = {'profile': profile}
    return render(request, "hello/front_page.html", context)


def request_stamps_view(request):
    qs = RequestStamp.objects.all().order_by('-id')[:10]
    json = serializers.serialize("json", qs)
    return HttpResponse(json, content_type="application/json")


def request_stamps_set_read_view(request):
    if request.method == "POST" and request.is_ajax():
        try:
            stamps = request.POST.getlist('requests[]', [])
            qs = RequestStamp.objects.filter(id__in=stamps)
            qs.update(new=False)
            pass
        except Exception as err:
            print err

        return HttpResponse("OK")

    return HttpResponseForbidden()


def user_register_view(request):
    return render(request, "registration/register.html", {})
