from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('projeto.core.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^contato/(\d+)/$', 'contato', name='contato'),
	url(r'^noticias/$', 'noticias', name='noticias'),
	url(r'^noticia/(?P<id_noticia>\d+)/$', 'noticia', name='noticia'),
	
    url(r'^admin/', include(admin.site.urls)),
)
