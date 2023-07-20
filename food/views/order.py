from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Order,
)
from ..serializers import (
    OrderSerializer,
)

class OrderCreateView(APIView):
    @swagger_auto_schema(request_body=OrderSerializer)
    def post(self, request: Request) -> Response:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class OrderListView(APIView):
    @swagger_auto_schema(responses={200: OrderSerializer(many=True)})
    def get(self, request: Request) -> Response:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
class OrderDetailView(APIView):
    @swagger_auto_schema(responses={200: OrderSerializer()})
    def get(self, request: Request, pk: int) -> Response:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
class OrderUpdateView(APIView):
    @swagger_auto_schema(request_body=OrderSerializer)
    def put(self, request: Request, pk: int) -> Response:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class OrderDeleteView(APIView):
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request: Request, pk: int) -> Response:
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    