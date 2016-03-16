
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'appconfig.views.index', name='index'),
    url(r'', include(frontend_urls)),
    url(r'', include('distribuidor.urls')),

    # url(r'^media/(?<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
]
