from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Order, ShippingAddress, Product, OrderItem
from base.serializers import OrderSerializer


class OrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses=OrderSerializer)
    def post(self, request):
        user = request.user
        data = request.data
        order_items = data['orderItems']

        if order_items and not len(order_items):
            return Response({'detail': 'No order Items'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = Order.objects.create(
            user=user,
            payment_method=data['paymentMethod'],
            tax_price=data['taxPrice'],
            shipping_price=data['shippingPrice'],
            total_price=data['totalPrice'],
        )

        # Create shipping address
        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postal_code=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
        )

        # create order items and set order to orderItem relationship
        for i in order_items:
            product = Product.objects.get(id=i['productId'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                quantity=i['quantity'],
                price=i['price'],
                image=product.image.url,
            )

            # Update stock

            product.count_in_stock -= item.quantity
            product.save()

        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
