from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import BlogSitemap

sitemaps = {
    'articles': BlogSitemap,
}

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('send_contact/', views.send_contact, name='send_contact'),
    path('politika-konfidencialnosti/', views.policy, name='policy'),
    path('spasibo-za-zayavku/', views.thanks, name='thanks'),
    path('statiya/<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<tag>/', views.article_category, name='post_category'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
