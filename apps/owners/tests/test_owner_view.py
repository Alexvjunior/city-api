import pytest


@pytest.mark.django_db
def test_get_0_all_owner(
        client,
        token_user,
        data_response_0):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.get(
        '/api/owners/', content_type='application/json', **headers)

    assert response.status_code == 200
    assert response.json() == data_response_0


@pytest.mark.django_db
def test_post_owner(
        client,
        token_user,
        data_create_owner,
        data_response_create_owner):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/owners/', data=data_create_owner, **headers)

    assert response.status_code == 201
    assert response.json() == data_response_create_owner


@pytest.mark.django_db
def test_post_owner_without_body(
        client,
        token_user,
        data_create_owner_without_body):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/owners/', **headers)

    assert response.status_code == 400
    assert response.json() == data_create_owner_without_body


@pytest.mark.django_db
def test_get_without_token(
        client,
        data_response_not_credential):

    response = client.get('/api/owners/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential


@pytest.mark.django_db
def test_post_without_token(
        client,
        data_response_not_credential):

    response = client.post('/api/owners/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential


@pytest.mark.django_db
def test_patch_without_token(
        client,
        data_response_not_credential):

    response = client.patch('/api/owners/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential


@pytest.mark.django_db
def test_delete_without_token(
        client,
        data_response_not_credential):

    response = client.delete('/api/owners/1/')

    assert response.status_code == 401
    assert response.json() == data_response_not_credential
