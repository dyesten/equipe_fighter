from django import forms
from projeto.core.models import Contato


class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
