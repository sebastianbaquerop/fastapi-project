import pytest
from fastapi.testclient import TestClient
import json


def test_health(test_client, test_health_response):
    """Health Check DB with success"""
    # Arrange
    data = test_health_response
    status_code = 200
    # Act
    response = test_client.get("/v2/health")
    # Assert
    assert response.status_code == 200
    assert response.json() == data


def test_get_user_value_error(
    test_client, mock_http_client, general_internal_server_error
):
    from unittest.mock import patch

    """Test that ValueError in service returns 500 error."""
    with patch(
        "app.api.v2.endpoints.users.UserAndPokemonService.get_users"
    ) as mock_service:
        # Arrange
        mock_service.side_effect = ValueError("Internal server error")
        # Act
        response = test_client.get("/v2/users/")
        # Assert
        assert response.status_code == 500
        assert response.json() == general_internal_server_error


def test_get_all_users_success_empty_registers(test_client):
    """Test of get all users with success"""
    # Arrange
    data = []
    status_code = 200
    # Act
    response = test_client.get("/v2/users/")
    # Assert
    assert response.status_code == status_code
    assert len(response.json()["data"]) == len(data)


def test_get_user_success_empty_register(test_client, general_error):
    """Test get error"""
    # Arrange
    user_id = "1"
    data = general_error
    status_code = 404
    # Act
    response = test_client.get("/v2/users/" + user_id)
    # Assert
    assert response.status_code == status_code
    assert response.json() == data


def test_post_user_success(
    test_client,
    user_and_pokemons_create_dto_mock,
    post_users_and_pokemons_response_success_mock,
):
    """Test for creating user successfully"""
    # Arrange
    status_code = 201
    payload = user_and_pokemons_create_dto_mock.model_dump(mode="json")
    mock_response = post_users_and_pokemons_response_success_mock.model_dump(
        mode="json"
    )
    # Act
    response = test_client.post("/v2/users", json=payload)
    assert response.status_code == status_code
    assert json.dumps(response.json(), sort_keys=True) == json.dumps(
        mock_response, sort_keys=True
    )


def test_post_user_with_pokemons_error(
    test_client, user_and_pokemons_create_dto_mock, post_error
):
    """Test create user error"""
    # Arrange
    status_code = 400
    payload = user_and_pokemons_create_dto_mock.model_dump(mode="json")
    mock_error_response = post_error
    # Act
    response = test_client.post("/v2/users", json=payload)
    # Assert
    assert response.status_code == status_code
    assert response.json() == mock_error_response


def test_get_user_by_id_success(
    test_client, get_user_and_pokemons_info_by_id_response_success_mock
):
    """Test to retrieve information of id user with success"""
    # Arrange
    user_id = "1"
    data = get_user_and_pokemons_info_by_id_response_success_mock.model_dump(
        mode="json"
    )
    status_code = 200
    # Act
    response = test_client.get("/v2/users/" + user_id)
    # Assert
    assert response.status_code == status_code
    assert response.json() == data


def test_put_success(
    test_client,
    user_and_pokemons_update_dto_mock,
    put_users_and_pokemons_response_success_mock,
):
    """Test to update complete info user with success"""
    # Arrange
    user_id = "1"
    payload = user_and_pokemons_update_dto_mock.model_dump(mode="json")
    mock_response = put_users_and_pokemons_response_success_mock.model_dump(mode="json")
    status_code = 200
    # Act
    response = test_client.put("/v2/users/" + user_id, json=payload)
    response_filtered = response.json()
    del response_filtered["data"]["updated_at"]
    del mock_response["data"]["updated_at"]
    # Assert
    assert response.status_code == status_code
    assert response_filtered == mock_response


def test_put_user_error_un_processable_content(
    test_client, user_and_pokemons_update_dto_mock, general_error
):
    """Test to update info user error"""
    # Arrange
    user_id = "2"
    payload = user_and_pokemons_update_dto_mock.model_dump(mode="json")
    data = general_error
    status_code = 422
    # Act
    response = test_client.put("/v2/users/" + user_id, json=payload)
    # Assert
    assert response.status_code == status_code
    assert response.json() == data


def test_patch_user_success(
    test_client,
    patch_user_and_pokemons_patch_dto_mock,
    patch_users_and_pokemons_response_success_mock,
):
    """Test to update specific info of user with success"""
    # Arrange
    user_id = "1"
    payload = patch_user_and_pokemons_patch_dto_mock.model_dump(mode="json")
    print(f"test_patch_success - payload ======> {payload}")
    mock_response = patch_users_and_pokemons_response_success_mock.model_dump(
        mode="json"
    )
    status_code = 200
    # Act
    response = test_client.patch("/v2/users/" + user_id, json=payload)
    response_filtered = response.json()
    del response_filtered["data"]["updated_at"]
    del mock_response["data"]["updated_at"]
    # Assert
    assert response.status_code == status_code
    assert response_filtered == mock_response


def test_patch_user_error_un_processable_content(
    test_client, patch_user_and_pokemons_patch_dto_mock, general_error
):
    """Test to update specific info of user error"""
    # Arrange
    user_id = "2"
    payload = patch_user_and_pokemons_patch_dto_mock.model_dump(mode="json")
    data = general_error
    status_code = 422
    # Act
    response = test_client.patch("/v2/users/" + user_id, json=payload)
    # Assert
    assert response.status_code == status_code
    assert response.json() == data


def test_delete_user_success_empty_register(test_client, delete_success):
    """Test of deleting user with success"""
    # Arrange
    user_id = "1"
    data = delete_success
    status_code = 200
    # Act
    response = test_client.delete("/v2/users/" + user_id)
    # Assert
    assert response.status_code == status_code
    assert response.json() == data


def test_delete_user_error(test_client, general_error):
    """Test of deleting user error"""
    # Arrange
    user_id = "2"
    data = general_error
    status_code = 406
    # Act
    response = test_client.delete("/v2/users/" + user_id)
    # Assert
    assert response.status_code == status_code
    assert response.json() == data
