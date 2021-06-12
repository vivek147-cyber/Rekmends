from django.contrib import admin
from .models import categories,Post,Review,Contact
# Register your models here.

class adminpost(admin.ModelAdmin):
    list_display=('title','image','category','subcategory')
    





admin.site.register(categories)
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(Post,adminpost)