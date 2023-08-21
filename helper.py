import requests

# API data
api_url = 'http://localhost:8000/api/test/'
username = 'example00user'
email = 'pcic095@gmail.com'
password = 'avunix9143'

# Create a dictionary with the request data
data = {
    'username': username,
    'email': email,
    'password': password
}

headers ={'Authorization': 'Token 0d36012d9312cfd27b370fa35f322004c263d9a2'}

# Make the POST request to the Django server
response = requests.post(api_url, data=data,headers=headers)

# Check the response status code

print('API data sent successfully')
print(response.headers)
if(response.status_code==200):
  print(response.text)