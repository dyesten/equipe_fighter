from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from projeto.core.forms import ContatoForm, PhotoForm
from projeto.core.models import Sobre, Contato, Noticia, Photo, Equipe, Modalidades, HorarioAulas
#from cloudinary.forms import cl_init_js_callbacks

G_CONTEXT = {'sobre':Sobre.objects.ultimo_sobre(), 'noticias':Noticia.objects.ultimas_noticias(),}

def enviarEmailComentario(obj):	
	titulo = 'Novo mensagem recebida pelo site'
	destino = 'dyesten.pt@gmail.com'
	texto = "\nNome: "+(obj.nome)+" \nE-mail: "+(obj.email)+" \nMensagem: "+(obj.comentario)
	
	send_mail(subject=titulo, message=texto, from_email=destino, recipient_list=[destino],	)

def home(request):
	c = {
		'fotos':Photo.objects.ultimas_fotos(),
		'carrosel':Photo.objects.carrosel_fotos(),
		'aulas':HorarioAulas.objects.all(),
		}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'index.html', context)

	
def equipe(request):
	c = {
		'equipe':Equipe.objects.all().order_by('dataCadastro'),
		}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'equipe.html', context)

	
def modalidades(request):
	c = {
		'modalidades':Modalidades.objects.all().order_by('modalidade'),
		}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'modalidades.html', context)


def contato(request):	
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if not form.is_valid():
			return render(request, 'contato.html', {'form':form} )

		obj = form.save()
		enviarEmailComentario(obj)	
		return HttpResponseRedirect('/contato_sucesso/%d/' % obj.pk)
		
	else:
		c = {'form':ContatoForm()}
		context = dict(c.items() + G_CONTEXT.items())
		return render(request, 'contato.html',  context)

def contato_sucesso(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	c = {'contato':contato}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'contato_sucesso.html', context)

def noticias(request):
	c = {
		'noticias':Noticia.objects.order_by('-dataAlteracao'),
		}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'noticias.html', context)
	
def noticia(request, slug):
	c = {
		'noticia':Noticia.objects.filter(slug=slug)
		}
	context = dict(c.items() + G_CONTEXT.items())
	return render(request, 'exibeNoticia.html', context)

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

	c = {
			'form':PhotoForm, 
			'photo':Photo.objects.order_by('-dataCadastro'), 
			'log':request.user.is_authenticated()
		}
	context = dict(c.items() + G_CONTEXT.items())
	
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
	return render(request, 'galeria.html', context)
