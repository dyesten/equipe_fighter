# coding: latin

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from cloudinary.models import CloudinaryField
from projeto.core.managers import NoticiasManager, PhotosManager, SobreManager

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cloudinary\.models\.CloudinaryField"])


class Sobre(models.Model):	 
	dataCadastro = models.DateTimeField(auto_now_add=True)	
	dataAlteracao = models.DateTimeField(auto_now=True)
	descricao = models.TextField()	
	objects = SobreManager()
	
	def __unicode__(self):
		return self.descricao
		
	class Meta:
		db_table = "tb_sobre"
		verbose_name = _('Descricao')
		verbose_name_plural = _('Descricoes Sobre')


class Noticia(models.Model):
	dataCadastro = models.DateTimeField(auto_now_add=True)
	dataAlteracao = models.DateTimeField(auto_now=True)
	titulo = models.CharField(max_length=100)
	slug = models.SlugField(_('Slug'), null=False, blank=False)
	noticia = HTMLField()
	imagem = models.FileField(upload_to='img', null=True, blank=True)
	user = models.ForeignKey(User)
	objects = NoticiasManager()
	
	def __unicode__(self):
		return self.titulo
	
	class Meta:
		db_table = "tb_noticias"
		verbose_name = _('noticia')
		verbose_name_plural = _('noticias')


class Contato(models.Model):
	nome = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	telefone = models.CharField(max_length=15)
	comentario = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)	
	
	def __unicode__(self):
		return self.nome		
	
	class Meta:
		db_table = "tb_contatos"
		verbose_name = _('contato')
		verbose_name_plural = _('contatos')


class Photo(models.Model):
	image = CloudinaryField('image', null=True, blank=True)
	dataCadastro = models.DateTimeField(auto_now_add=True)
	comentario = models.TextField(null=True, blank=True)
	carrosel = models.BooleanField()
	
	objects = PhotosManager()
	
	def __unicode__(self):
		return self.image.public_id
	
	class Meta:
		verbose_name = _('imagem')
		verbose_name_plural = _('imagens')

class Equipe(models.Model):
	foto = CloudinaryField('foto', null=True, blank=True)
	nome = models.CharField(max_length=100, null=False, blank=False)
	facebook = models.CharField(max_length=250, null=True, blank=True)
	descricao = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.nome
	
	class Meta:
		verbose_name = _('membro')
		verbose_name_plural = _('membros')
		
class HorarioAulas(models.Model):
	modalidade = models.CharField(max_length=100, null=False, blank=False)
	descricao = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)
	dataAlteracao = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.modalidade
	
	class Meta:
		verbose_name = _('aula')
		verbose_name_plural = _('aulas')

class Modalidades(models.Model):
	imagem = CloudinaryField('imagem', null=True, blank=True)
	modalidade = models.CharField(max_length=100, null=False, blank=False)
	descricao = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)
	dataAlteracao = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.modalidade
	
	class Meta:
		verbose_name = _('modalidade')
		verbose_name_plural = _('modalidades')

class Parceiros(models.Model):
	imagem = CloudinaryField('imagem', null=True, blank=True)
	parceiro = models.CharField(max_length=100, null=False, blank=False)
	descricao = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)
	dataAlteracao = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.parceiro
	
	class Meta:
		verbose_name = _('parceiro')
		verbose_name_plural = _('parceiros')
'''
class FilaTeste(models.Model):
	name = models.CharField(_('Nome'), max_length=255)
	user = models.ForeignKey(User)

	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name = _('nome')
		verbose_name_plural = _('nomes')
'''