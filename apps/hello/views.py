from django.shortcuts import render

from apps.hello.models import Profile


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
    return render(request, "hello/contact.html", context)


def contact_page_hardcoded(request):
    return render(request, "hello/contacts_hardcoded.html", {})
