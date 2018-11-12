from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^say/$', views.say),
    url(r'^haha/talk/$', views.talk),
    url(r'^(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.test)
]