from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost, Project

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['core:home', 'core:about', 'core:services', 'core:projects', 'core:blog', 'core:contact']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.completion_date 