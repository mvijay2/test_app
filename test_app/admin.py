from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Events, hhdata,CustomUser,Resources, Gallery, Team, geomap
# Register your models here.
#admin.site.register(table name (class in models ))
from .forms import CustomUserChangeForm, CustomUserCreationForm


admin.site.register(Events)
admin.site.register(hhdata)
admin.site.register(Gallery)
admin.site.register(Resources)
admin.site.register(Team)
admin.site.register(geomap)



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form=CustomUserChangeForm
    
    model=CustomUser
    list_display=('email', 'is_staff', 'is_active')
    list_filter=('email','is_staff', 'is_active')
    fieldsets=(
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','groups','user_permissions',)}),
    )

    add_fieldsets=(
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','password1', 'password2','is_staff','is_active')}
            ),
    )

    search_fields=('email',)
    ordering=('email',)

admin.site.register(CustomUser, CustomUserAdmin)