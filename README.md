# url_conversion_app

Recruitment task to convert given original url to a shorter version or return the original url from shorten version.

Tests are included in `url_conversion/tests.py`

URL API to test:

GET `http://127.0.0.1:8000/url_conversion`
To obtain an original url from shorten url simply write url as a query param e.g.
`http://127.0.0.1:8000/url_conversion?url=http://localhost:8000/abcde1`

POST `http://127.0.0.1:8000/url_conversion/`
To save an original url with the shorter url simply put data in request body
