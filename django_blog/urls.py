from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from blog.views import post_detail, user_login, blog_posts, faq, about, singup
import django.views.defaults
from django.views.static import serve
urlpatterns = [
    url(r'^', include('blog.urls'), name='blog'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', user_login,  name='blog_login'),
    url(r'^logout/', logout, kwargs={'next_page': '/login/'}, name='blog_logout'),
    url(r'^blog/post/$', blog_posts,  name='blog_posts'),
    url(r'^blog/post/(?P<id>[0-9]+)/$', post_detail, name='blog_post_detail'),
    url(r'^faq/$', faq,  name='blog_faq'),
    url(r'^about/$', about,  name='blog_about'),
    url(r'^singup/$', singup,  name='blog_singup'),

    url(r'404/$', django.views.defaults.page_not_found),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)