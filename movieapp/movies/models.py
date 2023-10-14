from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


class Movie(models.Model):
    def __str__(self):
        return self.movie_name

    movie_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    homepage = models.BooleanField(default=False)
