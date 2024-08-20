from django.contrib import sitemaps
from django.urls import reverse
from django.utils import timezone
from Blog.models import Blog



class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["home_page", "privacy_policy", "terms_of_service", "refund_policy", "about_us"]

    def location(self, item):
        return reverse(item)

    def get_latest_lastmod(self):
        today = timezone.localtime(timezone.now())
        return today


class BlogsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        blogs = list(Blog.objects.filter(publish=True))
        return blogs

    def location(self, item):
        absolute_url = reverse('blog_detail', kwargs={'pk':item.pk, 'slug':item.slug})
        return absolute_url

    def get_latest_lastmod(self):
        today = timezone.localtime(timezone.now())
        return today
