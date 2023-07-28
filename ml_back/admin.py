from django.contrib import admin
from .models import User
from .forms import CustomUserAdmin
from ml_api.models import CustomToken
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from rest_framework.authtoken.admin import TokenAdmin

    
    
# Register the CustomAPIKey model with the customized admin class
#admin.site.register(CustomAPIKey,CustomAPIKeyAdmin)
id="4f15b121e0f94280a3649a29dcfa3b8c"
#api_key = CustomAPIKey.objects.create_key(name='MyAPIKey',id=id)
#print(api_key)
key="H3qkYxXl.QQDH35AtC2wq0B3LfV51F5sEtCi2rpmH"
#h=CustomAPIKey.objects.get_from_key(key)
#print(h)
#print(len(CustomAPIKey.objects.get(key)))
#print(CustomAPIKey.objects.lol())
#print(dir(CustomAPIKey.objects))
# Register the custom User model and its Admin class

#print(dir(CustomUserAdmin))

admin.site.register(User,CustomUserAdmin)

#TokenAdmin.search_fields = ('user__username',)
    

#token =CustomToken.objects.filter(user_id="123ae13ccdc04d49a09699acab0f283e").order_by('created').first()


#print(token.key)       
admin.site.register(CustomToken)