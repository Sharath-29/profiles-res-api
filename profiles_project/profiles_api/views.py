from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "gives you the most control over your application logic",
            "is mapped manually to urls"
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})