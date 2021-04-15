from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Slink,Ulink,Clink,Contact

admin.site.site_header='C-url admin'

admin.site.register(Slink)
admin.site.register(Ulink)
admin.site.register(Clink)
admin.site.register(Contact)