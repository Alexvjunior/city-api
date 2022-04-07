from rest_framework import serializers

from apps.owners.models import OwnerModel


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerModel
        fields = ("__all__")
