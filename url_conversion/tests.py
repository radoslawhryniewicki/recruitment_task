from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from unittest.mock import patch

from .exceptions import URLModelNotInDBException
from .models import URLShortener



class URLConversionViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.conversion_url = reverse("url_conversion")

    @patch("url_conversion.views.generate_shorten_url")
    def test_post_request(self, mock_generate_shorten_url):
        mock_generate_shorten_url.return_value = "http://localhost:8000/abcdd1"
        response = self.client.post(
            self.conversion_url, {"original_url": "http://example.com"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "original_url": "http://example.com",
                "shorten_url": "http://localhost:8000/abcdd1",
            },
        )

    @patch("url_conversion.views.generate_shorten_url")
    def test_post_request_returns_400_for_invalid_url(self, mock_generate_shorten_url):
        mock_generate_shorten_url.return_value = "http://localhost:8000/abcdd1"
        response = self.client.post(
            self.conversion_url, {"original_url": "invalid_url"}, format="json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertTrue("error" in response.data)

    @patch("url_conversion.views.get_shortener_url")
    def test_get_request(self, mock_get_shortener_url):
        mock_get_shortener_url.return_value = URLShortener(
            original_url="http://example.com",
            shorten_url="http://localhost:8000/abcdd1",
        )
        response = self.client.get(
            self.conversion_url, {"shorten_url": "http://localhost:8000/abcdd1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "original_url": "http://example.com",
                "shorten_url": "http://localhost:8000/abcdd1",
            },
        )

    @patch("url_conversion.views.get_shortener_url")
    def test_get_request_returns_404_when_no_url_in_db(self, mock_get_shortener_url):
        mock_get_shortener_url.side_effect = URLModelNotInDBException(
            "No matching shorten URL found in the database"
        )
        response = self.client.get(
            self.conversion_url, {"shorten_url": "http://localhost:8000/abcdd1"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, mock_get_shortener_url.side_effect.args[0])
