from apiV2.payloads.auth import (
    auth_default_payload,
    wrong_password_payload,
    wrong_username_payload
    )
from playwright.sync_api import APIResponse

endpoint="/auth/login"

def test_authentication(config:dict, requests):
    response:APIResponse=requests.post(config["base_url"]+endpoint, data=auth_default_payload())
    assert response.ok
    assert "token" in response.json()

def test_authentication_wrong_username(config, requests):
    response=requests.post(config["base_url"]+endpoint, data=wrong_username_payload())
    assert response.status==401

def test_authentication_wrong_password(config, requests):
    response=requests.post(config["base_url"]+endpoint, data=wrong_password_payload())
    assert response.status==401