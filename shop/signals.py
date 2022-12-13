from django.db.models.signals import post_save
from .utils import convert_image_to_webp

from .models import Product


def product_post_save(sender, instance, created, *args, **kwargs):
    if instance.image:
        convert_image_to_webp(instance.image.path)


post_save.connect(product_post_save, sender=Product)
