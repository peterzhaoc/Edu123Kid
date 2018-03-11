from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from courses.models import *

admin.site.register(CourseBase)
admin.site.register(Course)
admin.site.register(Class)
