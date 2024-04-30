from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .exceptions import URLModelInDBException, URLModelNotInDBException
from .db import create_shortener_url, get_original_url
from .serializers import URLSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class URLConversionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = URLSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
           
        try:
            db_url_shortener = create_shortener_url(
                original_url=serializer.validated_data["url"]
            )
            return JsonResponse({"shorten_url": db_url_shortener.shorten_url})
        except URLModelInDBException as e:
            return Response(e.args, status=400)
        
    def get(self, request, *args, **kwargs):
        serializer = URLSerializer(data=request.GET)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        try:
            db_original_url = get_original_url(
                shorten_url=serializer.validated_data["url"]
            )
            return JsonResponse({"original_url": db_original_url})
        except URLModelNotInDBException as e:
            return Response(e.args, status=404)

        

            
            
            

# @api_view(["POST", "GET"])
# def url_conversion_view(request):
#     if request.method == "POST":
#         serializer = URLSerializer(data=request.data)
#         if not serializer.is_valid():
#             return HttpResponse("URL is malformed.", status=400)
#         try:
#             db_shortener_url = create_shortener_url(
#                 original_url=serializer.validated_data["url"]
#             )
#         except URLModelInDBException as e:
#             return HttpResponse(e.args, status=400)

#         return JsonResponse({"shortened_url": db_shortener_url.shorten_url})

#     elif request.method == "GET":
#         serializer = URLSerializer(data=request.GET)
#         if not serializer.is_valid():
#             return HttpResponse("URL is malformed.", status=400)
        # try:
        #     db_original_url = get_original_url(
        #         shorten_url=serializer.validated_data["url"]
        #     )
        # except URLModelNotInDBException as e:
        #     return HttpResponse(e.args, status=404)

        # return JsonResponse({"original_url": db_original_url})
