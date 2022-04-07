import pytest
from apps.cars.apps import CarsConfig

@pytest.mark.django_db
def test_config_payment_file_app():
    assert CarsConfig.name == "apps.cars"