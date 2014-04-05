from django.contrib import admin
from projeto.core.models import Noticia

class NoticiasAdmin(admin.ModelAdmin):		
	fieldsets = [
		('Informe um titulo para sua noticia', {'fields':['titulo']}),
		('Informe a noticia', {'fields':['noticia']}),
		('Selecione uma imagem', {'fields':['imagem']}),
	]
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
	
	
	
	
admin.site.register(Noticia, NoticiasAdmin)
'''
class FilaTesteAdmin(admin.ModelAdmin):
	list_display = ('name','user')
	exclude = ('user',)
'''
'''
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super(FilaTesteAdmin, self).save(request, obj, form, change)
'''

#admin.site.register(FilaTeste, FilaTesteAdmin)