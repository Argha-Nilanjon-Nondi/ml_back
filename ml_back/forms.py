from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from ml_api.models import CustomToken
from django.contrib import messages
from django import forms
from django.urls import path
from django.urls import re_path
from django.urls import resolve
from django.utils.html import format_html
from urllib.parse import quote as urlquote
from django.utils.translation import gettext as _, ngettext
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields=()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields=()

        
class TokenInline(admin.StackedInline):
    model = CustomToken
    can_delete = False
    
    def get_extra(self, request, obj=None, **kwargs):
        return 0

    def get_readonly_fields(self, request, obj=None):
        # Specify the 'created_at' field as read-only when editing the inline model
        if obj:
            return ['created',"machine"]
        return []
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # If the user is a superuser, show all data
            return qs
        else:
            # Show only data related to the logged-in user
            return qs.filter(user=request.user)
         
    
    def has_add_permission(self, request, obj=None):
        return False
 
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = [TokenInline]
    model = User

    list_display = (
                  'username', 
                  'email', 
                  'is_active',
                  'is_staff', 
                  'is_superuser', 
                  'last_login',
    )
    
    list_filter = (
                    'is_active', 
                    'is_staff', 
                    'is_superuser',
                    "last_login"
    )
                
    fieldsets = (
                (None, {'fields': ('username', 'email' ,"id", 'password')}),
                ('Permissions', {'fields': ('is_staff', 'is_active',
                'is_superuser', 'groups',"last_login" ,'user_permissions')}),
                
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password1','password2','is_staff','is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    def get_readonly_fields(self, request, obj=None):
        # Specify the fields to be read-only when editing an existing user
        if obj:
            return ('username',"id", 'email', 'last_login')
        # Specify the fields to be read-only when adding a new user
        return ('last_login',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # If the user is a superuser, show all data
            return qs
        else:
            # Show only data related to the logged-in user
            return qs.filter(email=request.user)

    def response_change(self, request, obj):
        """
        Determine the HttpResponse for the change_view stage.
        """
        IS_POPUP_VAR = '_popup'

        if IS_POPUP_VAR in request.POST:
            opts = obj._meta
            to_field = request.POST.get(TO_FIELD_VAR)
            attr = str(to_field) if to_field else opts.pk.attname
            value = request.resolver_match.kwargs['object_id']
            new_value = obj.serializable_value(attr)
            popup_response_data = json.dumps({
                'action': 'change',
                'value': str(value),
                'obj': str(obj),
                'new_value': str(new_value),
            })
            return TemplateResponse(request, self.popup_response_template or [
                'admin/%s/%s/popup_response.html' % (opts.app_label, opts.model_name),
                'admin/%s/popup_response.html' % opts.app_label,
                'admin/popup_response.html',
            ], {
                'popup_response_data': popup_response_data,
            })

        opts = self.model._meta
        preserved_filters = self.get_preserved_filters(request)

        msg_dict = {
            'name': opts.verbose_name,
            'obj': format_html('<a href="{}">{}</a>', urlquote(request.path),
            obj.email),
        }
        print(msg_dict)
        if "_continue" in request.POST:
          
            msg = format_html(
                _('The {name} “{obj}” was changed successfully. You may edit it again below.'),
                **msg_dict
            )
            
            self.message_user(request, msg, messages.SUCCESS)
            redirect_url = request.path
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)

        elif "_saveasnew" in request.POST:
            msg = format_html(
                _('The {name} “{obj}” was added successfully. You may edit it again below.'),
                **msg_dict
            )
            self.message_user(request, msg, messages.SUCCESS)
            redirect_url = reverse('admin:%s_%s_change' %
                                   (opts.app_label, opts.model_name),
                                   args=(obj.pk,),
                                   current_app=self.admin_site.name)
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)

        elif "_addanother" in request.POST:
            msg = format_html(
                _('The {name} “{obj}” was changed successfully. You may add another {name} below.'),
                **msg_dict
            )
            self.message_user(request, msg, messages.SUCCESS)
            redirect_url = reverse('admin:%s_%s_add' %
                                   (opts.app_label, opts.model_name),
                                   current_app=self.admin_site.name)
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)

        else:
            msg = format_html(
                _('The {name} “{obj}” was changed successfully.'),
                **msg_dict
            )
            self.message_user(request, msg, messages.SUCCESS)
            return self.response_post_save_change(request, obj)
