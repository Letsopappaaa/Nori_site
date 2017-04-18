from django.contrib import admin
from .models import upload, blog_post


class uploadsAdmin(admin.ModelAdmin):
    class Meta:
        model = upload

class blog_postsAdmin(admin.ModelAdmin):
    class Meta:
        model = blog_post

admin.site.register(upload, uploadsAdmin)
admin.site.register(blog_post, blog_postsAdmin)