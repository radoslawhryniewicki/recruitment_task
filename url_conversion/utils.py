from django.utils.crypto import get_random_string

from .const import DOMAIN_URL


def generate_shorten_url(code_length=5):
    return DOMAIN_URL + get_random_string(code_length)
