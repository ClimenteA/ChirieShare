from django.shortcuts import render


def anunturi(request):
    return render(request, "view_listings.html")