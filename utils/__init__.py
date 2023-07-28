from rest_framework.response import Response
from .api_status_code import custom_code
import hashlib
import re

def set_msg(status_dict,data=None):
  if(data is None):
    response = Response()
  if(data is not None):
    response=Response(data)
  response["Custom-Code"]=status_dict["code"]
  response["Custom-Msg"]=status_dict["msg"]
  return response    

def set_error_msg(serializer):
  response = Response()
  field_name=list(serializer.errors)[0]
  error_name=str(serializer.errors[field_name][0])
  error_dict=custom_code[error_name]
  response["Custom-Code"]=error_dict["code"]
  response["Custom-Msg"]=error_dict["msg"]
  return response    

def encrypt_sha256(plain_string):
    sha256_hash = (hashlib.sha256(plain_string.encode())).hexdigest()
    return sha256_hash
    

def is_valid_username(username):
    pattern = r'^[a-zA-Z0-9_]{3,}$'
    if re.match(pattern, username):
        return True
    else:
        return False
        
        
def is_valid_email(email):
    allowed_hosts = ["example.com","gmail.com" ,"domain.com", "yourdomain.com"]
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False    
        
def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#%^&*])?[A-Za-z\d@$!#%^&*]{8,}$'
    pattern=r''
    if re.match(pattern, password):
        return True
    else:
        return False
