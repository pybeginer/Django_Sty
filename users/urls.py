from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^say/$', views.say),
    url(r'^haha/talk/$', views.talk),
    url(r'^(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.test),
    url(r'^str_query/$', views.string_query),
    url(r'^req_body/$', views.req_body),
    url(r'^body_json/$', views.body_json)

]