# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    max_num = 1
    can_delete = False

class MentorProfileInline(admin.StackedInline):
    model = MentorProfile
    max_num = 1
    can_delete = False

class ProfileTypeAdmin(admin.ModelAdmin):
    inlines = [StudentProfileInline, MentorProfileInline,]

#class MentorProfileAdmin(admin.ModelAdmin):
#inlines = [MentorProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(UserProfile, ProfileTypeAdmin)
admin.site.register(StudentProfile)
admin.site.register(MentorProfile)
