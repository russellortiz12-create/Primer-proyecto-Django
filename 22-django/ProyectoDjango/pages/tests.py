from django.test import TestCase
from django.urls import reverse

from .models import Page


class PageNavigationTests(TestCase):
    def test_homepage_shows_home_and_visible_pages_but_not_about_link(self):
        Page.objects.create(
            title='Página de prueba',
            content='Contenido de prueba',
            slug='pagina-prueba',
            visible=True,
        )

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/"')
        self.assertContains(response, 'Inicio')
        self.assertNotContains(response, 'Sobre Nosotros')
        self.assertContains(response, 'href="/pagina/pagina-prueba"')
        self.assertContains(response, 'Página de prueba')

    def test_hidden_pages_are_not_in_navigation(self):
        Page.objects.create(
            title='Página oculta',
            content='Contenido oculto',
            slug='pagina-oculta',
            visible=False,
        )

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Página oculta')
