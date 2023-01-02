from django.urls import path
from .views import films, series, books

urlpatterns = [
    path('films/', films, name="blog-films"),
    path('series/', series, name="blog-series"),
    path('books/', books, name="blog-books"),

]

