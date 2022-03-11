from fastapi_users.authentication import JWTAuthentication

SECRET = "wf2455efdgefg#@"

jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login"
)