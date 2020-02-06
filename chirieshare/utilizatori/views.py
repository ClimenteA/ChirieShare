from django.shortcuts import render


def inregistrare(request):
    return render(request, "register.html")

