from django.core.files.storage import FileSystemStorage
from django.utils.html import mark_safe
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token
from ml_api.tasks import denoise_audio_client
from utils.fs_system import CustomFileSystemStorage
from colorama import Fore
from utils import generate_filename
import os
import uuid

class CustomToken(Token):
    """
    Customization of Token model from rest_framework.authtoken.models
    """
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key=models.CharField(max_length=100,blank=False)
    machine=models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
      return str(self.user)
  


upload_storage=CustomFileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,"music"),base_url=os.path.join(settings.MEDIA_URL,"music"))
denoised_storage=CustomFileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,"denoised"),base_url=os.path.join(settings.MEDIA_URL,"denoised"))

class CustomMusic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="ID")
    name = models.CharField(max_length=200,default="Untitled")
    user = models.ForeignKey(
                             settings.AUTH_USER_MODEL, 
                              related_name='musics',
                              on_delete=models.CASCADE,
                            )
    audio_file = models.FileField(storage=upload_storage)
    denoised_audio_file = models.FileField(storage=denoised_storage,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
      
        is_audio_updated=False
        
        try:
            this = CustomMusic.objects.get(id=self.id)
            if this.audio_file != self.audio_file:
               is_audio_updated=True
            """
            try to find record . if found and matched , it means user is trying to update a object .
            If database filename(this) and upload filename(self) is same ,it means file is same .
            """
            
        except CustomMusic.DoesNotExist:
              is_audio_updated=True
              print("Error Not found")
              # if record is not found , it means user is adding a new record and new file will be added 

        if is_audio_updated==False:
           return super().save(*args, **kwargs)
            # if audio is not created or updated then further processing is not need
        
        if is_audio_updated==True:
           denoise_audio_client.delay(input_filepath=self.audio_file.path,email=self.user.email,id=self.id)
           # if audio is updated , the audio will be sent to DENOISE_URL to denoisify . It is an asynchronous process
        
           return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
      """
      it is assumed that every object will have a audio file , but it is not required that every object will hold denoised audio
      """
      try:
         os.remove(self.audio_file.path) #audio file must be present 
         os.remove(self.denoised_audio_file.path)# denoised audio file may be present
      except Exception as e:
         print(e)
      super().delete(*args, **kwargs)
    
    def __str__(self):
      return str(self.user)
   
    @property
    def audio_file_display(self):
        """
        Show a audio player in admin interface for normal audio file
        """
        return mark_safe(f'<audio controls name="media"><source src="{self.audio_file.url}" type="audio/mpeg"></audio>')
        
    @property
    def id_display(self):
        return self.id
        
    @property
    def denoised_audio_file_display(self):
        """
        if object has denoised audio file , show a audio player in admin interface for denoised audio file ,
        else a text will be shown
        """
        if(self.denoised_audio_file==""):
           return mark_safe("<p>Audio is not ready yet</p>")
        return mark_safe(f'<audio controls name="media"><source src="{self.denoised_audio_file.url}" type="audio/mpeg"></audio>')
        