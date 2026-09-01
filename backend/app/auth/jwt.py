# JWT config
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    return "fake-jwt-token"
