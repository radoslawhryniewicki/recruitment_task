from rest_framework.views import APIView
from rest_framework.response import Response


from .exceptions import URLModelNotInDBException
from .db import get_shortener_url
from .serializers import URLShortenerSerializer
from .utils import generate_shorten_url


class URLConversionView(APIView):
    def post(self, request, *args, **kwargs):
        data = {**request.data, "shorten_url": generate_shorten_url()}
        serializer = URLShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors}, status=400)

    def get(self, request, *args, **kwargs):
        try:
            db_shortener_url = get_shortener_url(shorten_url=request.GET["shorten_url"])
            serializer = URLShortenerSerializer(db_shortener_url)
            return Response(serializer.data)
        except URLModelNotInDBException as e:
            return Response(e.args[0], status=404)
