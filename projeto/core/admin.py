# coding: latin
from django.contrib import admin
from projeto.core.models import Sobre, Noticia, Photo, Equipe, Modalidades, HorarioAulas
from projeto.core.forms import PhotoForm
from django.utils.translation import ungettext, ugettext as _

#from django.conf.urls import patterns, include, url #utilizado no teste do PhotoAdmin
#from django.template.response import TemplateResponse

import cloudinary.uploader

class SobreAdmin(admin.ModelAdmin):
	fieldsets = [
		('Informe a descrição', {'fields':['descricao']}),
	]

	#se houver um ou mais de um, ele nao permite adicionar mais
	def has_add_permission(self, request):
		if(Sobre.objects.count() >= 1):
			return False
		return True


class NoticiasAdmin(admin.ModelAdmin):
	fieldsets = [
		('Informe um titulo para sua noticia', {'fields':['titulo','slug']}),
		
		('Informe a noticia', {'fields':['noticia']}),
		('Selecione uma imagem', {'fields':['imagem']}),
	]
	prepopulated_fields = {'slug': ('titulo',)}#garante o preenchimento automatico do slug, baseado no nome digitado
	
	exclude = ('user',)
	list_display = ('titulo', 'dataCadastro', 'dataAlteracao', 'noticiaAlterado')
	list_filter = ['dataCadastro', 'dataAlteracao', 'titulo']
	search_fields = ['titulo', 'noticia', 'dataCadastro', 'dataAlteracao']
	
	
	def noticiaAlterado(self, request):
		return (request.dataAlteracao > request.dataCadastro)
	noticiaAlterado.boolean = True
	noticiaAlterado.short_description = 'Alterada?'
	
	#salva o pk - id user
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()
	
class PhotoAdmin(admin.ModelAdmin):
	#actions = None #desabilita todas as acoes
	actions = ['delete_imgs']
	
	fieldsets = [	
		('Selecione uma imagem', {'fields':['image', 'comentario','carrosel']} ),
	]
	list_display = ('imagemImg','dataCadastro','imagemCarrosel', )
	list_per_page = 10
	
	def imagemImg(self, request):
		return '<a href="%s"><img width="100" height="150" alt="imagem nao disponivel" \
				src="http://res.cloudinary.com/fighter/image/upload/c_fill,h_150,w_100/%s"></a>'%(request.id,request.image.public_id)
	imagemImg.allow_tags = True
	imagemImg.short_description = 'imagem'
	
	def imagemCarrosel(self, request):
		return request.carrosel == True
	imagemCarrosel.boolean = True
	imagemCarrosel.short_description = 'imagem'

	
	def save_model(self, request, obj, form, change):
		#for obj in obj: #olhar para habilitar com o multiple. no cloudinary ele inseriu, porque no BD nao?
		#se for de uma alteracao, apagar o arquivo e subir de novo no cloudinary.
		if change and 'image' in form.changed_data:
			img = Photo.objects.get(id=obj.id)
			#invalidate = True, forca uma invalidacao no cache, caso ocorra o carregamento de uma imagem e possa gerar a mesma id
			cloudinary.uploader.destroy(img.image.public_id, invalidate = True)
		
		super(PhotoAdmin, self).save_model(request, obj, form, change)
		
		'''
		for f in request.FILES.getlist('image'):
			obj.image = f
			obj.save()
			#x = cloudinary.uploader.upload(f)
			#obj.image = x['public_id']
		'''
		
		
		
	def delete_model(self, request, obj):
		img = Photo.objects.get(id=obj.id)
		#deleta imagem no cloudinary e posteriormente do bd
		cloudinary.uploader.destroy(img.image.public_id, invalidate = True)
		img.delete()

	#limpa a action padrao delete_selected
	def get_actions(self, request):
		actions = super(PhotoAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions
	
	#action delete imagens
	def delete_imgs(self, request, obj):
		qtd = len(obj)
		for o in obj.all():
			img = Photo.objects.get(id=o.id)
			#deleta imagem no cloudinary e posteriormente do bd
			cloudinary.uploader.destroy(img.image.public_id, invalidate = True)
			img.delete()
		
		
		msg = ungettext(
			u'%d imagem foi apagada.',
			u'%d imagens foram apagadas.',
			qtd
		)
		self.message_user(request, msg % qtd)
		
		'''
		# Display the confirmation page
		return TemplateResponse(request, PhotoAdmin.delete_selected_confirmation_template or [
			"admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.model_name),
			"admin/%s/delete_selected_confirmation.html" % app_label,
			"admin/delete_selected_confirmation.html"
		], context, current_app=PhotoAdmin.admin_site.name)
		'''
		
	delete_imgs.short_description = 'Deletar imagens selecionadas'
	
	
	#https://lincolnloop.com/static/slides/2010-djangocon/customizing-the-admin.html#slide61
	#change_list_template = 'diretorio_templates_projeto/nome_template.html'


class EquipeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Membro', {'fields':['nome', 'descricao', 'facebook', 'foto']}),
	]
	
	list_display = ('nome', 'descricao', 'dataCadastro')
	list_filter = ['dataCadastro']
	search_fields = ['nome', 'descricao']
	
	list_per_page = 10

	
class HorarioAulasAdmin(admin.ModelAdmin):
	fieldsets = [
		('Modalidade', {'fields':['modalidade', 'descricao']}),
	]
	
	list_display = ('modalidade', 'descricao', 'dataCadastro')
	list_filter = ['dataCadastro']
	search_fields = ['modalidade', 'descricao']
	
	list_per_page = 10
	
class ModalidadesAdmin(admin.ModelAdmin):
	fieldsets = [
		('Aulas', {'fields':['modalidade', 'descricao', 'imagem']}),
	]
	
	list_display = ('modalidade', 'descricao', 'dataCadastro')
	list_filter = ['dataCadastro']
	search_fields = ['modalidade', 'descricao']
	
	list_per_page = 10
	
admin.site.register(Sobre, SobreAdmin)
admin.site.register(Noticia, NoticiasAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(HorarioAulas, HorarioAulasAdmin)
admin.site.register(Modalidades, ModalidadesAdmin)

#admin.site.register(FilaTeste, FilaTesteAdmin)