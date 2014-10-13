# coding: utf-8
from django.test import TestCase
from projeto.core.forms import ContatoForm

class EquipeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/equipe/')
	
	def test_get(self):		
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'equipe.html')
	
	