# coding: utf-8
from django.test import TestCase
from projeto.core.forms import ContatoForm

class ModalidadesTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/modalidades/')
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'modalidades.html')