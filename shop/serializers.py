
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['image'] = self.image_field_display(obj)
        return data

    def image_field_display(self, obj):
        image = {
            'path': None,
            'formats': []
        }
        if obj.image:
            image = {
                'path': obj.get_image_path_without_format(),
                'formats': obj.get_image_formats()
            }

        return image