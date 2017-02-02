from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'attendence.views.home'),
    url(r'^getdata/$', 'attendence.views.getdata'),
    url(r'^getattendence/', 'attendence.views.getattendence'),
    url(r'^saveattendence/', 'attendence.views.saveattendence'),
]
