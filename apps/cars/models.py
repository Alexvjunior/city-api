from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.owners.models import OwnerModel

class CarsColors(models.TextChoices):
        YELLOW = 'Y', _('Yellow Color')
        BLUE = 'B', _('Blue Color')
        GREY = 'G', _('Grey Color')

class CarsModels(models.TextChoices):
        CONVERTIBLE = 'CO', _('Convertible Model')
        SEDAN = 'SE', _('Sedan Model')
        HATCH = 'HA', _('Hatch Model')


class CarModel(models.Model):

    color = models.CharField(
        max_length=1,
        choices=CarsColors.choices
    )

    car_model = models.CharField(
        max_length=2,
        choices=CarsModels.choices
    )

    owner = models.ForeignKey(OwnerModel, models.CASCADE)