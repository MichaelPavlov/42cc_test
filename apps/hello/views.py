from django.shortcuts import render


def contact_page(request):
    """
    Implements contact view.
    :param request:
    :return:
    """
    return render(request, "hello/contact.html", {})


def contact_page_hardcoded(request):
    return render(request, "hello/contacts_hardcoded.html", {})
