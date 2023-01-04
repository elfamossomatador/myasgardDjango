from django.conf.urls.static import static
from django.urls import path

from DocBlog import settings
from .views import films, series, books

urlpatterns = [
    path('films/', films, name="blog-films"),
    path('series/', series, name="blog-series"),
    path('books/', books, name="blog-books"),
]

