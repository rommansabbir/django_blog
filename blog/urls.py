from django.conf.urls import url
from blog.views import index, post_detail
urlpatterns = [
    url(r'^$', index, name='blog_index'),

]