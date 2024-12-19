import pytest
from api.endpoints.auth import auth_login
from playwright.sync_api import APIResponse

def test_authentication(config:dict, requests):
    response:APIResponse=auth_login(config, requests)
    assert response.ok
    assert "token" in response.json()

def test_authentication_wrong_username(config, requests):
    response=auth_login(config, requests, payload={"username":"wrong"})
    assert response.status==401

def test_authentication_wrong_password(config, requests):
    response=auth_login(config, requests, payload={"username":"wrong"})
    assert response.status==401