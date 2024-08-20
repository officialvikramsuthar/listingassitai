"""
URL configuration for listingassitai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from .sitemaps import StaticViewSitemap, BlogsSitemap
from django.contrib.sitemaps.views import sitemap
from sitepages.urls import urlpatterns as site_urls

sitemaps = {
    "static": StaticViewSitemap,
    "blogs": BlogsSitemap,
}


urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blogs/', include('Blog.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('178107ba5fa4459d8b8a15028f4b0b1b.txt', TemplateView.as_view(template_name="indexnow.txt", content_type='text/plain')),
]

urlpatterns = urlpatterns + site_urls
