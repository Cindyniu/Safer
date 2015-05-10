from django.conf.urls import patterns

from safer.views import hello, camera_capture

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^camera/$', camera_capture),
)
