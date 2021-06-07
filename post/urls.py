from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.Index_view.as_view()),
    url(r'^page/(\d+)$', views.Index_view.as_view()),
    url(r'^post/(\d+)$', views.Post_detail.as_view()),
    url(r'^footer/$', views.Footer.as_view()),
    url(r'^category/(\d+)$', views.queruPostByCreated),
    url(r'^archive/(\d+)/(\d+)$', views.queryPostByCreated),

]
