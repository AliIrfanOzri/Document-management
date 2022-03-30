from django.contrib import admin

# Register your models here.
from manage_docs.models import *
admin.site.register(Folders)
admin.site.register(Digital_Documents)
admin.site.register(Topics)