"""Views for the core app"""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """Returns successful Response."""
    return Response({'healthy': True})
