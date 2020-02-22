from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello , current_datetime

urlpatterns = [
     url(r'^admin/', include(admin.site.urls)),
     url(r'^hello/$', hello),
     url(r'^date/$' , current_datetime),
]
