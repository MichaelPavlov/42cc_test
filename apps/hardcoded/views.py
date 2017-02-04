from django.shortcuts import render


def contact_page_hc(request):
    return render(request, "hardcoded/requests.html", {})


def edit_contact_hc(request):
    return render(request, "hardcoded/edit_contact.html", {})
