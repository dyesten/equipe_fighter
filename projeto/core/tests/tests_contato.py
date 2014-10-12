# coding: utf-8
from django.test import TestCase
from projeto.core.forms import ContatoForm

class ContatoTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/contato/')
	
	def test_get(self):		
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'contato.html')
	
	def test_campos(self):
		form = ContatoForm()
		self.assertItemsEqual(['nome', 'email', 'telefone', 'comentario'], form.fields)
	
	def test_html(self):
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 5)
		self.assertContains(self.resp, 'type="text"', 2)
		self.assertContains(self.resp, 'type="email"', 1)
		self.assertContains(self.resp, '<textarea ', 1)

'''
class ContatoSucessoTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/contato_sucesso/1', args=[1])
	
	def test_get(self):		
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'contato_sucesso.html')
'''