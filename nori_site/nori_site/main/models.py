from django.db import models



dimensions_choices = (
    ('small', 'small'),
    ('medium', 'medium'),
    ('large', 'large')
    )

blog_post_pic_pos = (
    ('blog_img','hhh'),
    # ('blog_img-20','-20%'),
    # ('blog_img-30','-30%'),
    # ('blog_img-40','-40%'),
    # ('blog_img-50','-50%'),
    # ('blog_img-60','-60%'),
    # ('blog_img-70','-70%'),
    # ('blog_img-80','-80%'),
    # ('blog_img-90','-90%'),
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

class blog_post(models.Model):
    title = models.TextField()
    upload_time = models.DateTimeField()
    content = models.TextField()
    cover_photos = models.ImageField(upload_to = 'cover_photos/%Y/%m')
    img_pos = models.CharField(max_length = 15, choices = blog_post_pic_pos, 
        default = 'blog_img')

    def __str__(self):
        return self.title