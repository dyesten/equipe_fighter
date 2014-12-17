# coding: latin
from django import forms
from projeto.core.models import Contato, Photo, Equipe, Modalidades

from cloudinary.forms import CloudinaryJsFileField, CloudinaryFileField


class ContatoForm(forms.ModelForm):
	nome = forms.CharField(max_length=200, error_messages={'required': 'Preencha seu nome.'})
	email = forms.EmailField(max_length=200, error_messages={'required': 'Preencha seu email.', 
																'invalid':'Preencha um email válido.'}
															)
	telefone = forms.CharField(max_length=15, required=False)
	comentario = forms.Textarea()
	
	class Meta:
		model = Contato

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
	
	imagem = CloudinaryJsFileField() #CloudinaryFileField()

	
class EquipeForm(forms.ModelForm):
	class Meta:
		model = Equipe
	foto = CloudinaryJsFileField()
	
class ModalidadesForm(forms.ModelForm):
	class Meta:
		model = Modalidades
	imagem = CloudinaryJsFileField()