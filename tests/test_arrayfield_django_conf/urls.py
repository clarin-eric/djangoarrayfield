from django.http import HttpResponse
from django.urls import re_path


def mock_view(request):
    return HttpResponse(status=200)


urlpatterns = [
    re_path('', mock_view),
]
