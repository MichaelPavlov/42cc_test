from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.hello.views import contact_page
from apps.hardcoded import urls as hardcoded_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hardcoded/', include(hardcoded_urls, namespace="hardcoded")),
    url(r'^$', contact_page, name="contact"),
)
