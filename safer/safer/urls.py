from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from safer.views import hello, camera_capture

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^camera/$', camera_capture),
)   

#add static urlpatterns
urlpatterns += staticfiles_urlpatterns()
