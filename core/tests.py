from django.test import TestCase
from core.models import FeriadosModel
from datetime import datetime

class FeriadosModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadosModel(
            nome=self.feriado,
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FeriadosModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)
        
    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)
        
    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)