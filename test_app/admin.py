from django.contrib import admin

# Register your models here.
from .models import Events, Farmersdata
# Register your models here.
#admin.site.register(table name (class in models ))

admin.site.register(Events)
admin.site.register(Farmersdata)

