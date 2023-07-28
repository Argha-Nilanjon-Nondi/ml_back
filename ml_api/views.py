"""
This part is important , The code in below add utils module
path to the python runtime
"""
#import os
#import sys
#current_dir = os.path.dirname(os.path.abspath(__file__))
#project_root = os.path.abspath(os.path.join(current_dir, '../'))
#sys.path.append(project_root)
from rest_framework.decorators import authentication_classes,permission_classes
from ml_api.authentication import CustomTokenAuthentication,CustomIsAuthenticated
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ml_back.models import User
from ml_api.models import CustomToken
from utils.api_status_code import custom_code
from utils import set_msg,set_error_msg
from middleware import username_format,email_format,password_format
import json
from .serializer.serializer import APILoginSerializer
#from rest_framework.authtoken.models import Token
   

@api_view(["POST"])
def login(request):
  
  request_data=request.data
  serializer = APILoginSerializer(data=request_data)
  if(serializer.is_valid()==False):
      return send_error_msg(serializer)
  
  user_email=request_data["email"]
  user_password=request_data["password"]
  user=authenticate(request,username=user_email,password=user_password)
  if(user is None):
    return set_msg(custom_code["email-password-invalid"])
    
  token=Token.objects.create(user=user)
  return set_msg(custom_code["login-success"],{
         "token":token.key
  })
  
  
@api_view(["POST"])
@authentication_classes([CustomTokenAuthentication])
#@permission_classes([CustomIsAuthenticated])
def test(request):
  """
  headers = {'Authorization': 'Token 2d13234aff2ee37207fdaac04f3bde3d3c121fca'}
  """
  user = request.user
  print(user.id)
  if(user.is_authenticated==False):
    return set_msg(custom_code["token-invalid"])
  return Response("Hi-000")


@api_view(["get"])
@username_format
@email_format
@password_format
def create_user(request):
  request_data=request.data
  user_name=request_data["username"]
  user_email=request_data["email"]
  user_password=request_data["password"]
  
  user=Users()
  user.user_name=user_name
  user.user_email=user_email
  user.set_password("Argha1392@BHD")
  user.full_clean()
  user.save()
  
  data={"msg":"Hi"}
  return Response(data)
