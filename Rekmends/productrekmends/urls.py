from django.urls import path
from .import views

from django.conf.urls.static import static

from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, StaticSitemap 



sitemaps = {
    'Post':PostSitemap,
    'static':StaticSitemap #add StaticSitemap to the dictionary
}


urlpatterns = [
    path("", views.index, name="homepage"),
    path("contactus/",views.contact,name="contact"),
    path("aboutus/",views.about,name="about"),
    path("category/",views.category,name="category"),
    path("blogs/",views.blog,name="blog"),
    path("blogdesc/<int:id>-<slug:slug>/",views.blogdesc,name="blogdesc"),
    path('submit_review/<int:post_id>/',
         views.submit_review, name='submit_review'),
    path('search/', views.search, name='search'),
    path('products/',views.products,name="products"),
    path('nav/',views.nav,name="nav"),
    path('footer/',views.footer,name="footer"),
    path('subscribe/',views.subscribe,name="subscribe"),
    path('consub/',views.consub,name="consub"),
    path('privacy/',views.privacy,name="privacy"),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)