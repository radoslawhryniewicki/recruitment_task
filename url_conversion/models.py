from django.db import models
from django.utils.crypto import get_random_string

from .const import DOMAIN_URL, CODE_LENGTH


class URLShortener(models.Model):
    original_url = models.URLField(max_length=100, unique=True)
    shorten_url = models.CharField(max_length=50, unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.shorten_url:
            self.shorten_url = DOMAIN_URL + get_random_string(CODE_LENGTH)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Shorten URL for {self.original_url} is {self.shorten_url}"
