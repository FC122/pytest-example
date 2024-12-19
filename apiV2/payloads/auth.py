
def auth_default_payload(payload:dict={})->dict:
    default_payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    return default_payload|payload

def wrong_password_payload()->dict:
    return auth_default_payload({"password":"wrong"})

def wrong_username_payload()->dict:
    return auth_default_payload({"username":"wrong"})