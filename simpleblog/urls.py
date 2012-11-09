from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', TemplateView.as_view(template_name='home.html')),
)
