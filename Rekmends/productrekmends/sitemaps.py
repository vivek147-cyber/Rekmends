from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse
 
 
class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Post.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_on

    
        
    
class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return ['homepage','contact','about','category','blog','search','products','privacy']

    def location(self, item):
        return reverse(item)