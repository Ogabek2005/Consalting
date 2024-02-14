from django.contrib import admin
from .models import *

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'link')
    list_display_links = ('image', 'title', 'link')
    search_fields = ( 'title',)

@admin.register(Statistiks)
class StatistiksAdmin(admin.ModelAdmin):
    list_display = ('student_count', 'countries', 'univer_count', 'experiens')

@admin.register(servise)
class serviseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'order')
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('image','full_name','universitet','deegry')
    list_display_links = ('image',)
    search_fields = ('full_name','universitet','deegry')
    list_filter = ('deegry','universitet')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'deegry','message')
    search_fields = ('first_name', 'last_name', 'contact_number')

@admin.register(Revyu)
class RevyuAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'full_name', 'universitet')
    list_display_links = ('image','full_name', 'universitet')
    search_fields = ( 'full_name', 'universitet')

@admin.register(Social_account)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('icon','social_name', 'order')
    list_display_links = ('icon','social_name')
    search_fields = ( 'icon','social_name')
    
