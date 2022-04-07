import pytest
from pytest_factoryboy import register
from apps.factories import OwnerFactory, CarFactory, UserFactory
from rest_framework.authtoken.models import Token

register(OwnerFactory, 'owner')
register(CarFactory, 'car')
register(UserFactory, 'user')


@pytest.fixture
def token_user(user):
    return Token.objects.create(user=user)


@pytest.fixture
def data_response_0_cars():
    return {
        'count': 0,
        'next': None,
        'previous': None,
        'results': []
    }


@pytest.fixture
def data_response_not_credential():
    return {
        'detail': 'Authentication credentials were not provided.'
    }


@pytest.fixture
def data_response_retrieve():
    return {
        'id': 1,
        'owner': {
            'id': 1,
            'shell_opportunity': False,
        },
        'color': 'Y',
        'car_model': 'SE'
    }

@pytest.fixture
def data_response_post_validation_error():
    return ['This owner already have 3 or more cars']


@pytest.fixture
def data_create_car(owner):
    return {
        "color": "Y",
        "car_model": "SE",
        "owner": owner.id
    }


@pytest.fixture
def data_response_create_car():
    return {
        'car_model': 'SE',
        'color': 'Y',
        'id': 1,
        'owner': 1
    }


@pytest.fixture
def data_response_create_car_without_body():
    return {
        'color': ['This field is required.'],
        'car_model': ['This field is required.'],
        'owner': ['This field is required.']
    }
