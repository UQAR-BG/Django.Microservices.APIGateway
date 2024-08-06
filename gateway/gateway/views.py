from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class UserMicroserviceView(APIView):
    def get(self, request):
        response = requests.get('http://localhost:8001/api/users/')
        return Response(response.json())

class ProductMicroserviceView(APIView):
    def get(self, request):
        response = requests.get('http://localhost:8002/api/products/')
        return Response(response.json())