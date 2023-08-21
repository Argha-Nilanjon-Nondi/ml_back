"""
Decorators for verifying condition after performing function in views.py
"""
from django.contrib.auth import authenticate
from rest_framework.response import Response
from utils.api_status_code import custom_code
from utils import (
                    is_valid_username,
                    is_valid_email,
                    is_valid_password,
                    set_msg
                  )
from ml_back.models import User

def username_format(view_func):
    """
    check if a username is present in the request body 
    And validate the username.
    Args:
       Request Object
    Rerurn:
       Response Object(if validation fails) 
    """
    def wrapped_func(request, *args, **kwargs):
        if("username" not in request.data):
            return set_msg("username-empty")
    
        username=request.data["username"]    
        if(is_valid_username(username)==False):
            return set_msg("username-invalid")
            
        return view_func(request, *args, **kwargs)
    return wrapped_func
    
def email_format(view_func):
    """
    check if a email is present in the request body 
    And validate the email.
    Args:
       Request Object
    Rerurn:
       Response Object(if validation fails) 
    """
    def wrapped_func(request, *args, **kwargs):
      
        if("email" not in request.data):
            return set_msg("email-empty")
        
        email=request.data["email"]    
        if(is_valid_email(email)==False):
            return set_msg("email-invalid")
            
        return view_func(request, *args, **kwargs)
    return wrapped_func    
    
def password_format(view_func):
    """
    check if a password is present in the request body 
    And validate the password
    Args:
       Request Object
    Rerurn:
       Response Object(if validation fails) 
    """
    def wrapped_func(request, *args, **kwargs):
      
        if("password" not in request.data):
            return set_msg("password-empty")
        
        password=request.data["password"]    
        if(is_valid_password(password)==False):
            return set_msg("password-invalid")
            
        return view_func(request, *args, **kwargs)
    return wrapped_func    
    
def is_token_valid(view_func):
     """
     check if a token valid 
     @authentication_classes is need .@authentication_classes will set 
     request.user.is_authenticated
     
     -----Code----
     @authentication_classes([CustomTokenAuthentication])
     @is_token_valid
     """
     def wrapped_func(request, *args, **kwargs):
         if(request.user.is_authenticated==False):
           return set_msg("token-invalid")
         return view_func(request, *args, **kwargs)
     return wrapped_func  
   
def is_authenticated(view_func):
     """
     check if a email and password is valid for a user, if 
     valid then set user in request object like 
     
     -----Code----
     request.user=user
     """
     def wrapped_func(request, *args, **kwargs):
         request_data=request.data
         user_email=request_data["email"]
         user_password=request_data["password"]
         user=authenticate(request,email=user_email,password=user_password)
         if(user is None):
            return set_msg("email-password-invalid")
         request.user=user
         return view_func(request, *args, **kwargs)
     return wrapped_func  
 
  
def is_email_exist(view_func):
    """
    check if a email is already exist . If exist then set
    error header code and message
    """
    def wrapped_func(request, *args, **kwargs):
        user_email=request.data["email"]
        is_exist=User.objects.filter(email=user_email).exists()
        print(is_exist)
        if(is_exist==True):
            return set_msg("email-already-exit")
           
        return view_func(request, *args, **kwargs)
    return wrapped_func