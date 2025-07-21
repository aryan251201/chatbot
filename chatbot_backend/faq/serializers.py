from rest_framework import serializers
from .models import FAQ

class FAQSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'embedding', 'created_at']
        read_only_fields = ['id', 'embedding', 'created_at']