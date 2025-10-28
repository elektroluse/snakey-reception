from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("access_token")
        if not token:
            return None
        try:
            validated_token = self.get_validated_token(token)
        except AuthenticationFailed as error:
            raise AuthenticationFailed(f"token validation failed:{str(error)}")
        try:
            user = self.get_user(validated_token)
            return user, validated_token
        except AuthenticationFailed as error:
            raise(f"Error retrieving user:{str(error)}")