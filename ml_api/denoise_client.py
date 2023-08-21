"""
It is just a helper code , you can delete it , if you do not like it 
It does not have any effect on project
"""

from django.conf import settings
from lib.cryptographic import (
                                load_key,
                                encrypt_file
                              )
import requests
import json
import base64
import urllib.parse

def denoise_audio_client(input_filepath): 
    """
    encrypt the audio file with public key and send the file to DENOISE_URL
    """
    loaded_public_key =  load_key(settings.PUBLIC_KEY_PATH)
    input_file=open(input_filepath,"rb")
    input_content=input_file.read()
    input_file.close()
    encrypted_content=encrypt_file(input_content, loaded_public_key)
    encoded_data = base64.b64encode(encrypted_content).decode()
    url = settings.DENOISE_URL  # Replace with the actual URL of the server endpoint
    data = {
          'file_name': input_filename,
          'file_content': encoded_data
          }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
    print('Data sent successfully')
    else:
    print('Failed to send data')
