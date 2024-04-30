from django.urls import path

from .views import URLConversionView

urlpatterns = [
    path("", URLConversionView.as_view(), name="url_conversion"),
]
