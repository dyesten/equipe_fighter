from django import forms
from projeto.core.models import Contato, Photo

from cloudinary.forms import CloudinaryJsFileField


class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
	image = CloudinaryJsFileField()