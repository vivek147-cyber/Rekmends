from django.urls import path
from .import views

from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path("", views.index, name="homepage"),
    path("contactus/",views.contact,name="conatct"),
    path("aboutus/",views.about,name="about"),
    path("category/",views.category,name="category"),
    path("blogs/",views.blog,name="blog"),
    path("blogdesc/<int:id>-<slug:slug>/",views.blogdesc,name="blogdesc"),
    path('submit_review/<int:post_id>/',
         views.submit_review, name='submit_review'),
    path('search/', views.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)