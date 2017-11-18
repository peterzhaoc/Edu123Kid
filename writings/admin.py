from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from writings.models import *

admin.site.register(Book)
admin.site.register(Img)
admin.site.register(WritingTask)
