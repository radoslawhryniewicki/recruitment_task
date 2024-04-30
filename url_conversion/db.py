from .exceptions import URLModelInDBException, URLModelNotInDBException
from .models import URLShortener
from django.db import IntegrityError


def create_shortener_url(original_url: str) -> URLShortener:
    try:
        return URLShortener.objects.create(original_url=original_url)
    except IntegrityError:
        raise URLModelInDBException("Original URL already exists in the database")


def get_original_url(shorten_url: str) -> str:
    try:
        url_db_object = URLShortener.objects.get(shorten_url=shorten_url)
        return url_db_object.original_url
    except URLShortener.DoesNotExist:
        raise URLModelNotInDBException("No matching shorten URL found in the database")
