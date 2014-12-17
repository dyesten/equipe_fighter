from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, TemplateView

from projeto.core.forms import ContatoForm, PhotoForm
from projeto.core.models import Sobre, Contato, Noticia, Photo, Equipe, Modalidades, HorarioAulas, Parceiros
#from cloudinary.forms import cl_init_js_callbacks

#G_CONTEXT = {'sobre':Sobre.objects.ultimo_sobre(), 'noticias':Noticia.objects.ultimas_noticias(),}

def enviarEmailComentario(obj):	
	titulo = 'Novo mensagem recebida pelo site'
	destino = 'thaiboxingfera@hotmail.com'
	texto = "\nNome: "+(obj.nome)+" \nE-mail: "+(obj.email)+" \nMensagem: "+(obj.comentario)
	
	send_mail(subject=titulo, message=texto, from_email=destino, recipient_list=[destino],	)

def get_sobre(request):
	sobre = Sobre.objects.ultimo_sobre()
	sobre = serializers.serialize("json",  sobre)
	return HttpResponse(sobre, content_type="text/javascript")

def get_top5_noticias(request):
	noticias = Noticia.objects.ultimas_noticias()
	noticias = serializers.serialize("json",  noticias)
	return HttpResponse(noticias, content_type="text/javascript")

'''
def hello(request):
	context = {
		'fotos':Photo.objects.ultimas_fotos(),
		'carrosel':Photo.objects.carrosel_fotos(),
		'aulas':HorarioAulas.objects.all(),
		}
	context = dict(c.items() + G_CONTEXT.items())
	return context
'''	
	
def home(request):
	context = {
		'fotos':Photo.objects.ultimas_fotos(),
		'carrosel':Photo.objects.carrosel_fotos().order_by('dataCadastro'),
		'aulas':HorarioAulas.objects.all(),
		}
	
	return render(request, 'index.html', context)

	
def equipe(request):
	context = {
		'equipe':Equipe.objects.all().order_by('dataCadastro'),
		}
	return render(request, 'core/equipe.html', context)

	
def modalidades(request):
	context = {
		'modalidades':Modalidades.objects.all().order_by('modalidade'),
		}
	return render(request, 'core/modalidades.html', context)


def contato(request):	
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if not form.is_valid():
			return render(request, 'core/contato.html', {'form':form} )

		obj = form.save()
		enviarEmailComentario(obj)	
		return HttpResponseRedirect('/contato_sucesso/%d/' % obj.pk)
		
	else:
		context = {'form':ContatoForm()}
		return render(request, 'core/contato.html',  context)

'''
def contato_sucesso(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	context = {'contato':contato}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'contato_sucesso.html', context)
'''
class ContatoSucesso(DetailView):
	model = Contato
	
	def get_context_data(self, **kwargs):
		context = super(ContatoSucesso, self).get_context_data(**kwargs)
		return context
	

def noticias(request):
	context = {
		'noticias':Noticia.objects.order_by('-dataAlteracao'),
		}
	return render(request, 'core/noticias.html', context)
	
def noticia(request, slug):
	context = {
		'noticia':Noticia.objects.filter(slug=slug)
		}
	return render(request, 'core/exibeNoticia.html', context)

'''
def galeria(request):
	context = {
				'photo':Photo.objects.order_by('-dataCadastro'),
				}
	return render(request, 'arquivos.html', context)


def arquivos(request):
	return render(request, 'arquivos.html', {'form':PhotoForm})
'''

def galeria(request):
	context = dict( backend_form = PhotoForm())
	
	fotos_album = Photo.objects.order_by('-dataCadastro')
	paginator = Paginator(fotos_album, 12)
	
	try:
		fotos = paginator.page(request.GET.get('page'))
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		fotos = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		fotos = paginator.page(paginator.num_pages)
	
	context = {
			'form':PhotoForm, 
			'photo':fotos, 
			'log':request.user.is_authenticated()
		}
	
	#print([e.image for e in Photo.objects.all()])
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		
		for f in request.FILES.getlist('image'):
			Photo(image=f, carrosel=False).save()
		'''
		context['posted'] = form.instance
		if form.is_valid():
			form.save()
		'''
	return render(request, 'core/galeria.html', context)

def parceiros(request):
	context = {
		'parceiros':Parceiros.objects.all().order_by('parceiro'),
	}
	return render(request, 'core/parceiros.html', context)