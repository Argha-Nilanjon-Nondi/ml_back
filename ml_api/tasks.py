from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from ml_api import models
from utils.fs_system import CustomFileSystemStorage
from celery import shared_task
from celery.signals import task_success
from lib.cryptographic import load_key,encrypt_file
import requests
import json
import base64
import urllib.parse
import os
    
    
@shared_task()
def denoise_audio_client(input_filepath,email,id): 
    """
    encrypt the audio file with public key and send the file to DENOISE_URL
    """
    head, filename = os.path.split(input_filepath)
    loaded_public_key =  load_key(settings.PUBLIC_KEY_PATH)
    input_file=open(input_filepath,"rb")
    input_content=input_file.read()
    input_file.close()
    encrypted_content=encrypt_file(input_content, loaded_public_key)
    encoded_data = base64.b64encode(encrypted_content).decode()
    url = settings.DENOISE_URL  # Replace with the actual URL of the server endpoint
    data = {
          'file_name': filename,
          'file_content': encoded_data
          }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
       filename = response.headers.get("content-disposition").split("filename=")[1]
       content = response.content
       models.denoised_storage.save(filename,ContentFile(content))
       
       send_mail(
          'Denoised audio is ready',
           f'Go to the link http://127.0.0.1:8000/admin/ml_api/custommusic/{id}/change/',
           'ml_back@django.com',
            [email],
            fail_silently=False,
        ) # send email to user to notify that denoised audio file is ready to be played
       
       print('Data sent successfully')
       return { "id":id,"filename":filename} # dict is not mandatary you can use any type of datatype
    else:
       print('Failed to send data')
       send_mail(
          'Operation is failed',
           f'Go to the link http://127.0.0.1:8000/admin/ml_api/custommusic/{id}/change/ and delete the record , upload the file in new record',
           'ml_back@django.com',
            [email],
            fail_silently=False,
        ) # send email to user to notify that denoised audio file is ready to be played
       
    

@task_success.connect(sender=denoise_audio_client)
def my_signal_handler(sender, **kwargs):
    """
    If denoised audio file is achieved then save the file name in the model 
    according to id .
    """
    result=kwargs["result"]
    models.CustomMusic.objects.filter(id=result["id"]).update(denoised_audio_file=result["filename"])
    print("Signals of celery runned successfully")
    