from rest_framework import serializers

from .models import URLShortener


class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortener
        fields = ["original_url", "shorten_url"]
