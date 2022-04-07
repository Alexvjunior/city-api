from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class OwnerModel(models.Model):

    shell_opportunity = models.BooleanField(default=True)

    name = models.CharField(max_length=50)

    document_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[MaxLengthValidator(11), MinLengthValidator(11)]
        )
