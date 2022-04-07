import pytest
from apps.owners.apps import OwnersConfig

@pytest.mark.django_db
def test_config_payment_file_app():
    assert OwnersConfig.name == "apps.owners"