from .exceptions import URLModelNotInDBException
from .models import URLShortener


def get_shortener_url(shorten_url: str) -> URLShortener:
    try:
        return URLShortener.objects.get(shorten_url=shorten_url)
    except URLShortener.DoesNotExist:
        raise URLModelNotInDBException("No matching shorten URL found in the database")
