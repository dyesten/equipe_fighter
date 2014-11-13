from django import forms
from projeto.core.models import Contato, Photo, Equipe, Modalidades

from cloudinary.forms import CloudinaryJsFileField


class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
	image = CloudinaryJsFileField()
	
class EquipeForm(forms.ModelForm):
	class Meta:
		model = Equipe
	foto = CloudinaryJsFileField()
	
class ModalidadesForm(forms.ModelForm):
	class Meta:
		model = Modalidades
	imagem = CloudinaryJsFileField()