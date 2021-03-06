from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import mainView, blogView, aboutView, detailView


urlpatterns = [
    url(r'blog/$', blogView, name = 'blog'),
    url(r'blog/(?P<slug>[\w-]+)/', detailView, name = 'detail'),
    url(r'about/', aboutView, name = 'about'),
    url(r'^$', mainView, name = 'main'),
]
