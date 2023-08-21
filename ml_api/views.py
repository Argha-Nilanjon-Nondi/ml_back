from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ml_api.authentication import (
                                     CustomTokenAuthentication,
                                     #CustomExpiringTokenAuthentication,
                                     CustomIsAuthenticated
                                  )
from ml_api.models import CustomToken
from ml_back.models import User
from utils.api_status_code import custom_code
from utils import set_msg,set_error_msg
from decorator import (
                        username_format,
                        email_format,
                        password_format,
                        is_token_valid,
                        is_authenticated,
                        is_email_exist
                      )
import pprint


@api_view(["post"])
@username_format
@email_format
@password_format
@is_email_exist
def create_user(request):
  """
  Create a user , a normal user (Not a stuff , nor a superuser)
  """
  request_data=request.data
  user_name=request_data["username"]
  user_email=request_data["email"]
  user_password=request_data["password"]
  user = User.objects.create_user(username=user_name, email=user_email,password=user_password)
  return set_msg("user-create-success")



@api_view(["POST"])
@email_format
@password_format
@is_authenticated
def login(request):
  """
  Login a user , after verifying everything and
  give a token in response object
  """
  token=CustomToken.objects.create(user=request.user,machine="ITOP")
  return set_msg("login-success",{
         "token":token.key
  })
  


@api_view(["POST"])
@authentication_classes([CustomTokenAuthentication])
def add_music(request):
  
  user = request.user
  user_details = vars(user)

  pprint.pprint(user_details)
  #print(request.user)
  """
  headers = {'Authorization': 'Token 2d13234aff2ee37207fdaac04f3bde3d3c121fca'}
  """
  return Response("Hi-000")


  
@api_view(["POST"])
@authentication_classes([CustomTokenAuthentication])
#@is_token_valid
def test(request):
  

  user = request.user
  user_details = vars(user)

  pprint.pprint(user_details)
  #print(request.user)
  """
  headers = {'Authorization': 'Token 2d13234aff2ee37207fdaac04f3bde3d3c121fca'}
  """
  return Response("Hi-000")

