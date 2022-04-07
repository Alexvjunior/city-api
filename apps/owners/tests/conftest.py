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
def data_response_0():
    return {
        'count': 0,
        'next': None,
        'previous': None,
        'results': []
    }


@pytest.fixture
def data_create_owner():
    return {
        "name": "TESTE",
        "document_number": "00000000000"
    }


@pytest.fixture
def data_response_create_owner():
    return {
        'id': 1,
        'shell_opportunity': False,
        'name': 'TESTE',
        'document_number': '00000000000'
    }


@pytest.fixture
def data_create_owner_without_body():
    return {
        'name': ['This field is required.'],
        'document_number': ['This field is required.']
    }


@pytest.fixture
def data_response_not_credential():
    return {
        'detail': 'Authentication credentials were not provided.'
    }
