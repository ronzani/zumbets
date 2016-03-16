from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^login/$', 'distribuidor.views.login_view', name='login'),
                       url(r'^logout/$', 'distribuidor.views.logout_view', name='logout'),
                       url(r'^pwd_reset/(?P<username>\d+)/(?P<hash_val>.+)/$', 'distribuidor.views.password_user_reset', name='password_user_reset'),
                       )