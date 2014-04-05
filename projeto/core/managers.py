# coding: latin
from django.db import models
#from django.db.models import Max
from datetime import time

'''
class KindContactManager(models.Manager):
	def __init__(self, kind):
		super(KindContactManager, self).__init__()
		self.kind = kind
		
	def get_query_set(self):
		qs = super(KindContactManager, self).get_query_set()
		qs = qs.filter(kind=self.kind)
		return qs
'''
class NoticiasManager(models.Manager):
	
	def ultimas_noticias(self):
		#qs = self.values('titulo', 'noticia').order_by('-dataCadastro')[:5]
		qs = self.order_by('-dataCadastro')[:5]		
		return qs	