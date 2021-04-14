from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Slink,Ulink,Clink

admin.site.register(Slink)
admin.site.register(Ulink)
admin.site.register(Clink)