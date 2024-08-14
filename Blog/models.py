from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    img_link = models.URLField(blank=True, null=True)
    interview_only = models.BooleanField

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title