from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.owners.models import OwnerModel
from apps.owners.serializers import OwnerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = OwnerSerializer
    queryset = OwnerModel.objects.all()
    http_method_names = ["post", "patch", "get", "delete"]
