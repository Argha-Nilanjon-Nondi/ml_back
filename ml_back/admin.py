from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token, TokenProxy
from ml_back.forms import (
                            CustomUserAdmin,
                            MusicAdmin,
                            TokenAdmin
                          )
                          
from ml_api.models import (
                            CustomToken,
                            CustomMusic
                          )

User = get_user_model()

admin.site.register(User,CustomUserAdmin)
admin.site.register(CustomMusic,MusicAdmin)
admin.site.register(LogEntry)
admin.site.register(CustomToken,TokenAdmin)