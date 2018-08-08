from rest_framework.views import APIView
from rest_framework.response import Response


class Ping(APIView):
    """
    Ping sample endpoint.
    """
    def get(self, request, format=None):
        return Response({'result': 'pong!'})
