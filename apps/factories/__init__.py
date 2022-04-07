import uuid
import factory

from faker import Faker
from factory.django import DjangoModelFactory

from apps.cars.models import CarModel
from apps.owners.models import OwnerModel
from apps.users.models import UserModel

fake = Faker('pt_BR')


class OwnerFactory(DjangoModelFactory):

    class Meta:
        model = OwnerModel

    name = factory.LazyAttribute(lambda x: fake.name())
    document_number = factory.LazyAttribute(lambda x: fake.company_id())


class CarFactory(DjangoModelFactory):

    class Meta:
        model = CarModel

    owner = OwnerModel()
    color = "Y"
    car_model = "SE"

class UserFactory(DjangoModelFactory):
    
    class Meta:
        model = UserModel

    username = factory.LazyAttribute(lambda x: fake.name())
    password = factory.LazyAttribute(lambda x: fake.name())

