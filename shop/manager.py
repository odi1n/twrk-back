from django.db import models
from django.db.models import Q


class ProductQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(sku__icontains=query))

        return self.filter(lookups)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)
