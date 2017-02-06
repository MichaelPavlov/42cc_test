from django.shortcuts import render


def user_register_view(request):
    return render(request, "registration/register.html", {})
