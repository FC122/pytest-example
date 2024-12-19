from api.payloads.auth import auth_default_payload
from playwright.sync_api import APIRequestContext, APIResponse

def auth_login(config:dict, requests:APIRequestContext, payload:dict={}, headers:dict={}, params:dict={})->APIResponse:
    """
    Makes auth_login request
    """
    return requests.post(
        f'{config["base_url"]}/auth/login', 
        data=auth_default_payload(payload),
        headers=headers,
        params=params
    )
