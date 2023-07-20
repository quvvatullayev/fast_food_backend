from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Product,
)
from ..serializers import (
    ProductSerializer,
)

class ProductCreateView(APIView):        
    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
            
class ProductListView(APIView):
    @swagger_auto_schema(responses={200: ProductSerializer(many=True)})
    def get(self, request: Request) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
                    
class ProductDetailView(APIView):
    @swagger_auto_schema(responses={200: ProductSerializer()})
    def get(self, request: Request, pk: int) -> Response:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
                            
class ProductUpdateView(APIView):
    @swagger_auto_schema(request_body=ProductSerializer)
    def put(self, request: Request, pk: int) -> Response:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ProductDeleteView(APIView):                                   
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request: Request, pk: int) -> Response:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    