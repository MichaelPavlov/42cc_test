from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.hardcoded import urls as hardcoded_urls
from apps.hello.views import contact_page, request_stamps_view, \
    request_stamps_set_read_view

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hardcoded/', include(hardcoded_urls, namespace="hardcoded")),
    url(r'^$', contact_page, name="contact"),
    url(r'^api/request-stamps/$', request_stamps_view, name="request-stamps"),
    url(r'^api/request-stamps-set-read/$', request_stamps_set_read_view,
        name="request-stamps-set-read"),
)
