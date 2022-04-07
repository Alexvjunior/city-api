import pytest
from pytest_factoryboy import register
from apps.factories import UserFactory
from rest_framework.authtoken.models import Token

register(UserFactory, 'user')


@pytest.fixture
def token_user(user):
    return Token.objects.create(user=user)


@pytest.fixture
def data_response_all_users():
    return {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': 1,
                'last_login': None,
                'is_superuser': False,
                'first_name': '',
                'last_name': '',
                'email': '',
                'is_staff': False,
                'is_active': True,
                'groups': [],
                'user_permissions': []
            }
        ]
    }


@pytest.fixture
def data_token_user(user):
    return {
        "username": user.username,
        "password": user.password
    }
