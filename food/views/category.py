from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Category,
)
from ..serializers import (
    CategorySerializer,
)

class CategoryCreateView(APIView):

    @swagger_auto_schema(request_body=CategorySerializer)
    def post(self, request: Request) -> Response:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class CategoryListView(APIView):
    
        @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
        def get(self, request: Request) -> Response:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
        
class CategoryDetailView(APIView):
        
            @swagger_auto_schema(responses={200: CategorySerializer()})
            def get(self, request: Request, pk: int) -> Response:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response(serializer.data)
            
class CategoryUpdateView(APIView):
            
            @swagger_auto_schema(request_body=CategorySerializer)
            def put(self, request: Request, pk: int) -> Response:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(instance=category, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            
class CategoryDeleteView(APIView):
            
            @swagger_auto_schema(responses={204: 'No Content'})
            def delete(self, request: Request, pk: int) -> Response:
                category = Category.objects.get(pk=pk)
                category.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    
