from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "gives you the most control over your application logic",
            "is mapped manually to urls"
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk=None):
        
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    """Test api viewset"""
    def list(self, request):
        """Run a hello message"""

        a_viewset = [
            'Uses action (list, create, destroy , retrieve , update , partially update)',
            'Automatically maps to URLs using Routers ',
            'Provides more functionality with less code'

        ]
        return Response({'message': 'hello!','a_viewset': a_viewset})

    def create(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        
        return Response({'http_method': 'DELETE'})
