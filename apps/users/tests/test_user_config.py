import pytest
from apps.users.apps import UsersConfig

@pytest.mark.django_db
def test_config_payment_file_app():
    assert UsersConfig.name == "apps.users"