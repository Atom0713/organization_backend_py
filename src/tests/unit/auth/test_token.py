import pytest

from src.service.auth.token import decode_auth_token, encode_auth_token


@pytest.mark.parametrize("user_id", [1])
def test_encode_auth_token(user_id):
    auth_token = encode_auth_token(user_id)
    assert isinstance(auth_token, str)


@pytest.mark.parametrize("expected_user_id", [1])
def test_dencode_auth_token(expected_user_id):
    auth_token = encode_auth_token(expected_user_id)
    assert isinstance(auth_token, str)
    assert decode_auth_token(auth_token) == expected_user_id
