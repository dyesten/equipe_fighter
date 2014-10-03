# coding: latin
from django.db import models	
from datetime import time

class SobreManager(models.Manager):
	def ultimo_sobre(self):
		qs = self.order_by('-dataAlteracao')[:1]
		return qs
		
class NoticiasManager(models.Manager):
	def ultimas_noticias(self):
		qs = self.order_by('-dataCadastro')[:5]		
		return qs

class PhotosManager(models.Manager):
	def ultimas_fotos(self):
		qs = self.order_by('-dataCadastro')[:6]
		return qs
		
	def carrosel_fotos(self):
		qs = self.filter(carrosel=True).order_by('-dataCadastro')
		return qs