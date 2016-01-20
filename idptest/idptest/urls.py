from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Required for login:
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # URLs for the IDP:
    url(r'^idp/', include('saml2idp.urls')),
]
