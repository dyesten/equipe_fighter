from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect #HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

from projeto.core.forms import ContatoForm
from projeto.core.models import Contato, Noticia

def enviarEmailComentario(obj):	
	titulo = 'Mensagem enviada pelo site'
	destino = 'dyesten.pt@gmail.com'
	texto = "\nNome: "+(obj.nome)+" \nE-mail: "+(obj.email)+" \nMensagem: "+(obj.comentario)
	
	#send_mail(subject=titulo, message=texto, from_email=destino, recipient_list=[destino],	)

def home(request):	
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)
	
def new(request):
	context = {
				'origem':'novo',
				'noticias':Noticia.objects.ultimas_noticias(),
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