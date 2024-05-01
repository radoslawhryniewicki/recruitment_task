# recuritment_task_url_conversion

Recruitment task to convert given original url to a shorter version or return the original url from shorten version.

**IMPORTANT: The sqlite db file is not included thus is necessary to run `python manage.py migrate` command before running a server**

Tests are included in `url_conversion/tests.py`

<br><br>
URL API to test:

### GET `http://127.0.0.1:8000/url_conversion`

To obtain an original url from shorten url simply write url as a query param e.g.

`http://127.0.0.1:8000/url_conversion?shorten_url=http://localhost:8000/abcde1`

### POST `http://127.0.0.1:8000/url_conversion/`

To save an original url with the shorter url simply put json data in request body e.g.
```
{
  "original_url": "https://www.google.pl"
}
```
