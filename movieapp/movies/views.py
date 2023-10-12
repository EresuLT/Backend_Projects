from django.shortcuts import render

category_list = [
    "Adventure",
    "Romantic",
    "Drama",
    "Comedy",
    "Science Fiction",
]

movie_list = [
    {
        "movie_name": "Movie 1",
        "description": "Movie 1 description",
        "image": "https://picsum.photos/200/300?random=1",
    },
    {
        "movie_name": "Movie 2",
        "description": "Movie 2 description",
        "image": "https://picsum.photos/200/300?random=2",
    },
    {
        "movie_name": "Movie 3",
        "description": "Movie 3 description",
        "image": "https://picsum.photos/200/300?random=3",
    },
    {
        "movie_name": "Movie 4",
        "description": "Movie 4 description",
        "image": "https://picsum.photos/200/300?random=4",
    },
]


def home(request):
    data = {"categories": category_list, "movies": movie_list}
    return render(request, "index.html", data)


def movies(request):
    return render(request, "movies.html")
