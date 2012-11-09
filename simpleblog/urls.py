from django.conf.urls.defaults import patterns, url

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^login$', "django.contrib.auth.views.login",
        {"template_name": "auth/login.html"}, name="login"),
    url('^logout$', "django.contrib.auth.views.logout",
        {"template_name": "auth/logged-out.html"}, name="logout"),
)
urlpatterns += patterns("simpleblog.content.views",
    url('^$', "index", name="index"),
)
