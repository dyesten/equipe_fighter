from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from projeto.core.forms import ContatoForm, PhotoForm
from projeto.core.models import Contato, Noticia, Photo

#from cloudinary.forms import cl_init_js_callbacks

def enviarEmailComentario(obj):	
	titulo = 'Novo mensagem recebida pelo site'
	destino = 'dyesten.pt@gmail.com'
	texto = "\nNome: "+(obj.nome)+" \nE-mail: "+(obj.email)+" \nMensagem: "+(obj.comentario)
	
	send_mail(subject=titulo, message=texto, from_email=destino, recipient_list=[destino],	)

def home(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)
	
def new(request):
	context = {
				'origem':'novo',
				'noticias':Noticia.objects.ultimas_noticias(),
				'fotos':Photo.objects.ultimas_fotos(),
				'carrosel':Photo.objects.carrosel_fotos(),
				'form':ContatoForm(),
				}
	return render(request, 'index.html', context)

def create(request):
	form = ContatoForm(request.POST)
	context = {
				'origem':'criando',
				'form':form,
				}
	if not form.is_valid():
		return render(request, 'index.html', context)

	obj = form.save()
	enviarEmailComentario(obj)	
	return HttpResponseRedirect('/contato/%d/' % obj.pk)
	
def contato(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	return render(request, 'contato_sucesso.html', {'contato':contato})
	
def noticias(request):
	context = {
				'noticias':Noticia.objects.order_by('-dataAlteracao'),
				}
	return render(request, 'noticias.html', context)
	
def noticia(request, slug):
	context = {
				'noticia':Noticia.objects.filter(slug=slug)
				}
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
	return render(request, 'arquivos.html', {'form':PhotoForm, 'photo':Photo.objects.order_by('-dataCadastro'), 'log':request.user.is_authenticated()})
