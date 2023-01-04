from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Product


def index(request):
    return render(request, "homepage.html")


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'blog/detail.html', context={"product": product})


def product_list(request, *args, **kwargs):
    products = Product.objects.all()

    if request.method == "GET":
        name = request.GET.get('reserch')
        if name is not None:
            products = Product.objects.filter(name__icontains=name)
        else:
            products = None

    return render(request, 'blog/list.html', context={"products": products})


