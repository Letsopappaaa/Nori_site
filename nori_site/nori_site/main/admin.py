from django.contrib import admin
from .models import upload, blog_post, about_post


class uploadsAdmin(admin.ModelAdmin):
    class Meta:
        model = upload

class blog_postsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title", )}
    

    class Meta:
        model = blog_post

class about_postAdmin(admin.ModelAdmin):
    class Meta:
        model = about_post


admin.site.register(upload, uploadsAdmin)
admin.site.register(blog_post, blog_postsAdmin)
admin.site.register(about_post, about_postAdmin)