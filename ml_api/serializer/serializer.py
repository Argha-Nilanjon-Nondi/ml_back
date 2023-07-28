from rest_framework import serializers
from django.core.exceptions import ValidationError

def validate_username(username):
    # Define your criteria for the username here.
    # For example, let's say we want the username to contain only alphanumeric characters.
    if "0" in username:
        raise ValidationError(
          "username-invalid"
        )

class APISerializer(serializers.Serializer):
  username=serializers.CharField(
                                 error_messages={
                                                    'required': "username-empty"
                                                }
                                )
                    
  email=serializers.EmailField(
      error_messages={
                    "required":"email-empty",
                    "invalid":"email-invalid"
                   })
                   
  password=serializers.CharField(max_length=100,
  error_messages={
                    "required":"password-empty",
                  
                   })
  exclude_fields = []
  
    
  
  def get_fields(self):
      fields = super().get_fields()
      for field in self.exclude_fields:
        fields.pop(field, default=None)
      return fields
  
  
#print(dir(APILoginSerializer))

class APILoginSerializer(APISerializer):
  exclude_fields=["username"]
  #username.validators