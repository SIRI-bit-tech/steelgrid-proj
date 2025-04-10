from django.contrib import admin
from .models import Service, Project, TeamMember, BlogPost, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completion_date', 'client')
    list_filter = ('category', 'completion_date')
    search_fields = ('title', 'description', 'client')
    date_hierarchy = 'completion_date'

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position', 'bio')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
