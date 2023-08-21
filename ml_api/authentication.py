from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from ml_api.models import CustomToken
import pytz

class CustomTokenAuthentication(TokenAuthentication):
    """
    Custom token authentication with expiring functionality
    """
    model = CustomToken
    
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        utc_now = timezone.now()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        
        if token.created < utc_now - settings.TOKEN_LIFESPAN:
            raise exceptions.AuthenticationFailed("Token has expired")

        return (token.user, token)

class CustomIsAuthenticated(IsAuthenticated):
    model=CustomToken
    