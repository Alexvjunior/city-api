from rest_framework import serializers

from apps.cars.models import CarModel
from apps.owners.serializers import OwnerSerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("__all__")

    def save(self, **kwargs):
        owner = self.validated_data.get("owner")

        cars_count = CarModel.objects.filter(
            owner=owner.id).count()

        if cars_count >= 3:
            raise serializers.ValidationError(
                "This owner already have 3 or more cars")

        owner.shell_opportunity = False
        owner.save()

        return super().save(**kwargs)


class CarRetrieveSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = CarModel
        fields = ("__all__")
