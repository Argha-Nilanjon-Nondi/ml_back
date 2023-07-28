from django.db import models
import uuid
from rest_framework.authtoken.models import Token
from django.conf import settings

class CustomToken(Token):
    #print("xxxx ==",dir(Token))
    machine=models.CharField(max_length=100)
    #key=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.ForeignKey(  # changed from OneToOne to ForeignKey
    settings.AUTH_USER_MODEL, related_name='tokens',
    on_delete=models.CASCADE,
     )
     
    property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
    
    def __str__(self):
      return str(self.user)