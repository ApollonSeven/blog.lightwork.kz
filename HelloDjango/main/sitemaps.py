from django.conf import settings
from django.contrib import sitemaps
from main.models import Articles

class BlogSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Articles.objects.filter()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, item):
        url = '/statiya/' + str(item.slug)
        return url
