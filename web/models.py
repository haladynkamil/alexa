from django.db import models


class Website(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=120)
    meta_description = models.CharField(max_length=255)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey('web.WebsiteCategory', on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class WebsiteCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField()


class WebPage(models.Model):
    website = models.ForeignKey('web.Website', on_delete=models.PROTECT)
    url = models.URLField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120)
    meta_description = models.CharField(max_length=255)



