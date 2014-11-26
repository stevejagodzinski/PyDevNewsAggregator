from django.db import models
from django.contrib.auth.models import User


class HtmlContent(models.Model):
    url = models.TextField()
    name = models.CharField(max_length=255)
    scraping_strategy = models.IntegerField()
    outer_content_selector = models.TextField()
    inner_content_selector = models.TextField()
    title_selector = models.TextField()
    ignore_first_n_posts = models.IntegerField(default=0)
    ignore_last_n_posts = models.IntegerField(default=0)
    date_parsing_strategy = models.IntegerField()
    date_selector = models.TextField()
    time_selector = models.TextField()
    enabled = models.BooleanField()
    users = models.ManyToManyField(User)