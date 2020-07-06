from django.contrib import admin
from .models import User, Profile, ProfileInterest, ProfileLanguage

@admin.register(ProfileInterest)
class ProfileInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'interest')
    list_display_links = ('id',)

@admin.register(ProfileLanguage)
class ProfileLanguageAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')
    inlines = [ProfileInline]
