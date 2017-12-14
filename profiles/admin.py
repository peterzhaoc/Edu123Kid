# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *


class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class StudentProfileAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline, ]

class MentorProfileAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(MentorProfile, MentorProfileAdmin)
