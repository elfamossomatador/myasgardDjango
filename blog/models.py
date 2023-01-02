from django.db import models
from django.urls import reverse

# Create your models here.
"""
Product
-Nom
-Description
-Image
-Lien
-Type(0/1/2 for Film/Serie/Book)
"""


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    link = models.CharField(max_length=256, blank=True)
    type = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


