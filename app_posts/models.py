from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'pk': self.pk})


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('news', 'Новости'),
        ('sport', 'Спорт'),
        ('tech', 'Технологии'),
    )
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
