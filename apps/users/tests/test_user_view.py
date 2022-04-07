import pytest


@pytest.mark.django_db
def test_get_all_owner(
        client,
        token_user,
        data_response_all_users):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.get(
        '/api/users/', content_type='application/json', **headers)

    data = response.json()

    assert response.status_code == 200
    del data["results"][0]['username']
    del data["results"][0]['password']
    del data["results"][0]['date_joined']
    assert data == data_response_all_users


@pytest.mark.django_db
def test_token_user(
        client,
        token_user,
        data_token_user):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/token/', data=data_token_user, **headers)

    assert response.status_code == 200
    assert response.json() == {"token": response.json().get("token")}


@pytest.mark.django_db
def test_token_user_without_body(
        client,
        token_user):

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/token/', **headers)

    assert response.status_code == 400
    assert response.json() == {'message': 'Bad request'}


@pytest.mark.django_db
def test_token_not_found_user(
        client,
        token_user):

    data = {"username": "not found", "password": "not found"}

    headers = {'HTTP_AUTHORIZATION': f'Token {token_user.key}'}
    response = client.post('/api/token/', data=data, **headers)

    assert response.status_code == 400
    assert response.json() == {"message":"User not Found"}


