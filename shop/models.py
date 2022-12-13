import os
from pathlib import Path

from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.manager import ProductManager
from shop.type import StatusType, Type


class Product(models.Model):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

        ordering = ['title']

    title = models.CharField(_('title'), max_length=255)
    sku = models.CharField(_('sku'), max_length=255, unique=True)
    slug = models.SlugField(_('slug'), max_length=255)

    category = models.ForeignKey(verbose_name=_('category'), to='Category', on_delete=models.PROTECT,
                                 related_name='products')

    description = models.TextField(_('description'), blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=11, decimal_places=2, default=0.00)
    image = models.ImageField(_('image'), upload_to='images/products', blank=True, null=True)
    status = models.CharField(_('status'), max_length=15, choices=StatusType.choices, default=StatusType.IN_STOCK)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_image_formats(self):
        """
        Return list image formats
        """
        formats = []
        if self.image:
            image_path = Path(self.image.path)
            image_dir = image_path.parent
            image_name = image_path.stem
            for file in image_dir.iterdir():
                if file.stem == image_name:
                    formats.append(file.suffix[1:])
        return formats

    def get_image_path_without_format(self):
        """
        Return image path
        """
        return os.path.splitext(self.image.url)[0]


class Category(models.Model):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

        ordering = ['title']

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    property_objects = models.ManyToManyField(verbose_name=_('properties'), to='PropertyObject')

    def __str__(self):
        return self.title


class PropertyObject(models.Model):
    class Meta:
        verbose_name = _('property object')
        verbose_name_plural = _('properties objects')

        ordering = ['title']

    title = models.CharField(_('title'), max_length=255)
    code = models.SlugField(_('code'), max_length=255)
    value_type = models.CharField(_('value type'), max_length=10, choices=Type.choices)

    def __str__(self):
        return f'{self.title} ({self.get_value_type_display()})'


class PropertyValue(models.Model):
    class Meta:
        verbose_name = _('property value')
        verbose_name_plural = _('properties values')

        ordering = ['value_string', 'value_decimal']

    property_object = models.ForeignKey(to=PropertyObject, on_delete=models.PROTECT)

    value_string = models.CharField(_('value string'), max_length=255, blank=True, null=True)
    value_decimal = models.DecimalField(_('value decimal'), max_digits=11, decimal_places=2, blank=True, null=True)
    code = models.SlugField(_('code'), max_length=255)

    products = models.ManyToManyField(to=Product, related_name='properties')

    def __str__(self):
        return str(getattr(self, f'value_{self.property_object.value_type}', None))
