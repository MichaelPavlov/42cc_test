from django.conf.urls import patterns, url

from apps.hardcoded.views import contact_page_hc, edit_contact_hc

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^contact/$', contact_page_hc, name="contact"),
    url(r'^edit-contact/$', edit_contact_hc, name="edit-contact"),
)
