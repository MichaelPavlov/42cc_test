import time
from django.shortcuts import render


def contact_page_hc(request):
    return render(request, "hardcoded/requests.html", {})


def edit_contact_hc(request):
    if request.is_ajax():
        time.sleep(3)
    return render(request, "hardcoded/edit_contact.html", {})
