#para ejecutar las pruebas debemos ocupar el siguiente comando en la consola: "python manage.py test laboratorio"

from django.test import TestCase   
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio inicial para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Test",
            ciudad="Ciudad Test",
            pais="Pais Test"
        )

    def test_laboratorio_data(self):
        # Verificar que los datos coincidan con los creados en setUpTestData
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Test")
        self.assertEqual(laboratorio.ciudad, "Ciudad Test")
        self.assertEqual(laboratorio.pais, "Pais Test")

class LaboratorioURLTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio inicial para pruebas de URLs
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Test URL",
            ciudad="Ciudad URL",
            pais="Pais URL"
        )

    def test_listar_laboratorios_url(self):
        # Verificar que la URL de listar laboratorios devuelva un HTTP 200
        response = self.client.get(reverse('laboratorio:listar_laboratorios'))
        self.assertEqual(response.status_code, 200)

    def test_usar_plantilla_listar_laboratorios(self):
        # Verificar que se use la plantilla correcta
        response = self.client.get(reverse('laboratorio:listar_laboratorios'))
        self.assertTemplateUsed(response, 'laboratorio/listar_laboratorios.html')

    def test_contenido_html_listar_laboratorios(self):
        # Verificar que el contenido HTML esperado esté presente
        response = self.client.get(reverse('laboratorio:listar_laboratorios'))
        self.assertContains(response, "Información de Laboratorios")
        self.assertContains(response, "Laboratorio Test URL")

    def test_editar_laboratorio_url(self):
        # Verificar que la URL de editar laboratorio devuelva un HTTP 200
        response = self.client.get(reverse('laboratorio:editar_laboratorio', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

    def test_eliminar_laboratorio_url(self):
        # Verificar que la URL de eliminar laboratorio devuelva un HTTP 200
        response = self.client.get(reverse('laboratorio:eliminar_laboratorio', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

