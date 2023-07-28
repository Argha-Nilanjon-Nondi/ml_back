"""
Actually this functions are not ideal Django middleware.
But can be use as middleware . They are used as decorators .
The code is written to apply middleware functionality on specific views
(see views.py)
Django does not provide functionality that a middleware can be applied to a 
specific path , route or view
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../'))
sys.path.append(project_root)

from rest_framework.response import Response
from utils.api_status_code import custom_code
from utils import is_valid_username,is_valid_email,is_valid_password


def username_format(view_func):
    """
    check if a username is in the request body 
    And validate the username.
    Args:
       Request Object
    Rerurn:
       Response Object(if validation fails) 
    """
    def middleware(request, *args, **kwargs):
      
        response = Response()
        if("username" not in request.data):
            error=custom_code["username-empty"]
            response["Custom-Code"]=error["code"]
            response["Custom-Msg"]=error["msg"]
            return response
        
        username=request.data["username"]    
        if(is_valid_username(username)==False):
            error=custom_code["username-invalid"]
            response["Custom-Code"]=error["code"]
            response["Custom-Msg"]=error["msg"]
            return response
            
        return view_func(request, *args, **kwargs)
    return middleware
    
def email_format(view_func):
    """
    check if a email is in the request body 
    And validate the email.
    Args:
       Request Object
    Rerurn:
       Response Object(if validation fails) 
    """
    def middleware(request, *args, **kwargs):
      
        response = Response()
        if("email" not in request.data):
            error=custom_code["email-empty"]
            response["Custom-Code"]=error["code"]
            response["Custom-Msg"]=error["msg"]
            return response
        
        email=request.data["email"]    
        if(is_valid_email(email)==False):
            error=custom_code["email-invalid"]
            response["Custom-Code"]=error["code"]
            response["Custom-Msg"]=error["msg"]
            return response
            
        return view_func(request, *args, **kwargs)
    return middleware    
    
def password_format(view_func):
    """
    check if a password is in the request body 
    And validate the password
    Args:
       Request Object
    Rerurn:
       Response Object(if validation fails) 
    """
    def middleware(request, *args, **kwargs):
      
        response = Response()
        if("password" not in request.data):
            error=custom_code["password-empty"]
            response["Custom-Code"]=error["code"]
            response["Custom-Msg"]=error["msg"]
            return response
        
        password=request.data["password"]    
        if(is_valid_password(password)==False):
            error=custom_code["password-invalid"]
            response["Custom-Code"]=error["code"]
            response["Custom-Msg"]=error["msg"]
            return response
            
        return view_func(request, *args, **kwargs)
    return middleware    