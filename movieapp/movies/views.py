from django.shortcuts import render
from .models import Category, Movie

category_list = [
    "Adventure",
    "Romantic",
    "Drama",
    "Comedy",
    "Science Fiction",
]

movie_list = [
    {
        "id": 1,
        "movie_name": "Movie 1",
        "description": "Movie 1 description",
        "image": "1stMovie.jpg",
        "homepage": True,
    },
    {
        "id": 2,
        "movie_name": "Movie 2",
        "description": "Movie 2 description",
        "image": "2ndMovie.jpg",
        "homepage": True,
    },
    {
        "id": 3,
        "movie_name": "Movie 3",
        "description": "Movie 3 description",
        "image": "3rdMovie.jpg",
        "homepage": False,
    },
    {
        "id": 4,
        "movie_name": "Movie 4",
        "description": "Movie 4 description",
        "image": "4thMovie.jpg",
        "homepage": False,
    },
]


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
