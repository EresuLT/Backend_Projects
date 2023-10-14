from django.shortcuts import render
from .models import Category, Movie

def home(request):
    data = {
        "categories": Category.objects.all(),
        "movies": Movie.objects.filter(homepage=True),
    }
    return render(request, "index.html", data)


def movies(request):
    data = {"categories": Category.objects.all(), "movies": Movie.objects.all()}
    return render(request, "movies.html", data)


def moviedetails(request, id):
    data = {"movie": Movie.objects.get(id=id)}
    return render(request, "details.html", data)
