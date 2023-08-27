from rest_framework import generics, mixins

from base.models import Product
from base.serializers import ProductSerializer


class ProductView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    """
    View for handling product data.
    This view combines the functionality of listing multiple products and retrieving
    a single product using the provided endpoints.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None):
        """
        Handle GET requests for the view.
        :param request: An HTTP request object.
        :param pk: Product ID for retrieving a specific product (default is None).
        :return: returns all products if pk was not provided, otherwise, returns a specific product
        """
        return self.retrieve(request, pk) if pk else self.list(request)
