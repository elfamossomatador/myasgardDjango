from django.shortcuts import render

from blog.models import Product


def films(request):
    products = Product.objects.all()

    return render(request, 'blog/films.html', context={"products": products})


def series(request):
    products = Product.objects.all()

    return render(request, 'blog/series.html', context={"products": products})


def books(request):
    products = Product.objects.all()

    return render(request, 'blog/books.html', context={"products": products})

