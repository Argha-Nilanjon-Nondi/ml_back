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

headers = {'Authorization': 'Token 2d13234aff2ee37207fdaac04f3bde3d3c121fca'}

# Make the POST request to the Django server
response = requests.post(api_url, data=data,headers=headers)

# Check the response status code
if response.status_code == 200:
    print('API data sent successfully')
    print(response.headers)
    print(response.text)
else:
    print('Failed to send API data')
