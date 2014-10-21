from django.conf.urls import patterns, include, url
from django.contrib import admin
from anybuy import settings
#from account.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anybuy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^index/$', 'account.views.index',name = 'index'),
    url(r'^$', 'account.views.index'),
    url(r'^register/$','account.views.register', name = 'register'),
    url(r'^login/$','account.views.login',name = 'login'),
    url(r'^logout/$','account.views.logout' ,name = 'logout'),
    url(r'^search/(?P<keyword>\w*)/$', 'account.views.search'),
    url(r'^commodity/id/(?P<id>\d*)/$', 'account.views.getCommodity'),

    url(r'^base_template/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    #url(r'^account/$', views.register, name='register'),
    #url(r'^account/register/$',views.register, name = 'register'),
)
