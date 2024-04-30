from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from unittest.mock import patch

from .exceptions import URLModelInDBException, URLModelNotInDBException


class URLConversionViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.conversion_url = reverse("url_conversion")

    @patch("url_conversion.views.create_shortener_url")
    def test_create_shortened_url(self, mock_create_shortener_url):
        mock_create_shortener_url.return_value.shorten_url = (
            "http://localhost:8000/abcd1"
        )
        response = self.client.post(
            self.conversion_url, {"url": "http://example.com/"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["shorten_url"], "http://localhost:8000/abcd1")

    @patch("url_conversion.views.create_shortener_url")
    def test_create_shortened_url_returns_400_for_duplication(
        self, mock_create_shortener_url
    ):
        mock_create_shortener_url.side_effect = URLModelInDBException()
        response = self.client.post(
            self.conversion_url, {"url": "http://example.com/"}, format="json"
        )
        self.assertEqual(response.status_code, 400)

    @patch("url_conversion.views.get_original_url")
    def test_get_original_url(self, mock_get_original_url):
        mock_get_original_url.return_value = "http://example.com/"
        response = self.client.get(
            self.conversion_url, {"url": "http://localhost:8000/abcdd1"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["original_url"], "http://example.com/")

    @patch("url_conversion.views.get_original_url")
    def test_get_original_url_not_found(self, mock_get_original_url):
        mock_get_original_url.side_effect = URLModelNotInDBException()
        response = self.client.get(
            self.conversion_url, {"url": "http://localhost:8000/abcdd1"}, format="json"
        )
        self.assertEqual(response.status_code, 404)
