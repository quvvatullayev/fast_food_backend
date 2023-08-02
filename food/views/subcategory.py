from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    SubCategory,
)
from ..serializers import (
    SubCategorySerializer,
)

class SubCategoryCreateView(APIView):
    @swagger_auto_schema(request_body=SubCategorySerializer)
    def post(self, request: Request) -> Response:
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
class SubCategoryListView(APIView):
    @swagger_auto_schema(responses={200: SubCategorySerializer(many=True)})
    def get(self, request: Request, pk:int) -> Response:
        subcategories = SubCategory.objects.filter(category_id=pk)
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)
            
class SubCategoryDetailView(APIView):
    @swagger_auto_schema(responses={200: SubCategorySerializer()})
    def get(self, request: Request, pk: int) -> Response:
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)
                
class SubCategoryUpdateView(APIView):
    @swagger_auto_schema(request_body=SubCategorySerializer)
    def put(self, request: Request, pk: int) -> Response:
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategorySerializer(instance=subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
                
class SubCategoryDeleteView(APIView):
                
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request: Request, pk: int) -> Response:
        subcategory = SubCategory.objects.get(pk=pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
     