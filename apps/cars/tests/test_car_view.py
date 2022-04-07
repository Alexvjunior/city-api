import pytest


@pytest.mark.django_db
def test_get_0_all_cars(
        client,
        token_user,
        data_response_0_cars):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.get(
        '/api/cars/', content_type='application/json', **headers)

    assert response.status_code == 200
    assert response.json() == data_response_0_cars


@pytest.mark.django_db
def test_post_car(
        client,
        token_user,
        data_create_car,
        data_response_create_car):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/cars/', data=data_create_car, **headers)

    assert response.status_code == 201
    assert response.json() == data_response_create_car


@pytest.mark.django_db
def test_post_car_and_retrieve(
        client,
        token_user,
        data_create_car,
        data_response_retrieve):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    client.post('/api/cars/', data=data_create_car, **headers)
    response = client.get('/api/cars/1/', data=data_create_car, **headers)

    data = response.json()

    assert response.status_code == 200
    del data["owner"]["name"]
    del data["owner"]["document_number"]
    assert response.json() == data_response_retrieve

@pytest.mark.django_db
def test_post_car_send_more_3_cars(
        client,
        token_user,
        data_create_car,
        data_response_post_validation_error):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    client.post('/api/cars/', data=data_create_car, **headers)
    client.post('/api/cars/', data=data_create_car, **headers)
    client.post('/api/cars/', data=data_create_car, **headers)
    response = client.post('/api/cars/', data=data_create_car, **headers)

    assert response.status_code == 400
    assert response.json() == data_response_post_validation_error


@pytest.mark.django_db
def test_post_car_without_body(
        client,
        token_user,
        data_response_create_car_without_body):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/cars/', **headers)

    assert response.status_code == 400
    assert response.json() == data_response_create_car_without_body


@pytest.mark.django_db
def test_get_without_token(
        client,
        data_response_not_credential):

    response = client.get('/api/cars/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential


@pytest.mark.django_db
def test_post_without_token(
        client,
        data_response_not_credential):

    response = client.post('/api/cars/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential


@pytest.mark.django_db
def test_patch_without_token(
        client,
        data_response_not_credential):

    response = client.patch('/api/cars/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential


@pytest.mark.django_db
def test_delete_without_token(
        client,
        data_response_not_credential):

    response = client.delete('/api/cars/1/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential
