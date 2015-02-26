from django.conf.urls import patterns, include, url
from django.contrib import admin
from SMS import SendTemplateSMS

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^get_sms/(?P<required>\d+)/(?P<optional>.*)/$', include(SendTemplateSMS.sendTemplateSMS)),

)
