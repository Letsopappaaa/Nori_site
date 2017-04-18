from django.db import models
from django.utils.text import slugify


dimensions_choices = (
    ('small', 'small'),
    ('medium', 'medium'),
    ('large', 'large')
    )


class upload(models.Model):
    title = models.TextField()
    upload_time = models.DateTimeField()
    upload_date = models.DateField()
    location = models.CharField(max_length = 35)
    post_dimensions = models.CharField(max_length = 15, 
        choices = dimensions_choices, default = 'small')
    photos = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.title


blog_img_choices = (
    ('none', 'top'),
    ('blog_img-10', '-10%lejjebb'),
    ('blog_img-30', '-30%lejjebb'),
    ('blog_img-50', '-50%lejjebb'),
    ('blog_img-70', '-70%lejjebb'),
    ('blog_img-90', '-90%lejjebb'),
    )


class blog_post(models.Model):
    title = models.CharField(max_length = 150)
    upload_time = models.DateTimeField()
    content = models.TextField()
    cover_photos = models.ImageField(upload_to = 'cover_photos/%Y/%m')
    image_position = models.CharField(choices = blog_img_choices,
        default = 'top', max_length = 25)
    slug = models.SlugField(max_length = 150)

    def __str__(self):
        return self.title


class about_post(models.Model):
    title = models.TextField()
    upload_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title