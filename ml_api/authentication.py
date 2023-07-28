from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ml_api.models import CustomToken
class CustomTokenAuthentication(TokenAuthentication):
    model = CustomToken
    

class CustomIsAuthenticated(IsAuthenticated):
    model=CustomToken
    
#print(dir(TokenAuthentication))
#obj=CustomTokenAuthentication()
#print("cc=000000",dir(obj))
#print(obj.authenticate_credentials(key="c91eb9f2e1db3513de40e3dedefd3227276"))
