from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.hello.views import contact_page, contact_page_hardcoded

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contact_page, name="contact"),
    url(r'^contacts_hardcoded/$', contact_page_hardcoded, name="contact"),
)
