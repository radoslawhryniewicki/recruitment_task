from django.db import models


class URLShortener(models.Model):
    original_url = models.URLField(max_length=100, unique=True)
    shorten_url = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Shorten URL for {self.original_url} is {self.shorten_url}"
