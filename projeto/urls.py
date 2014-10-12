from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('projeto.core.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^equipe/$', 'equipe', name='equipe'),
    url(r'^modalidades/$', 'modalidades', name='modalidades'),
    url(r'^contato/$', 'contato', name='contato'),
	url(r'^noticias/$', 'noticias', name='noticias'),
	url(r'^galeria/$', 'galeria', name='galeria'),
	url(r'^contato_sucesso/(\d+)/$', 'contato_sucesso', name='contato_sucesso'),
	url(r'^noticia/(?P<slug>[a-zA-Z0-9-_\.]+)/$', 'noticia', name='noticia'),
	
    url(r'^admin/', include(admin.site.urls)),
	(r'^tinymce/', include('tinymce.urls')),
)
