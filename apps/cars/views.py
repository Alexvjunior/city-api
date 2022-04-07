from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.cars.models import CarModel
from apps.cars.serializers import CarRetrieveSerializer, CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    http_method_names = ["post", "patch", "get", "delete"]


    def list(self, request, *args, **kwargs):
        self.serializer_class = CarRetrieveSerializer
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CarRetrieveSerializer
        return super().retrieve(request, *args, **kwargs)