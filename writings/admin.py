from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from writings.models import *

class WritingTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'mentor_end_date', 'editor', 'finaleditor', 'pay', 'state', )

admin.site.register(Book)
admin.site.register(Img)
admin.site.register(WritingTask,WritingTaskAdmin)
