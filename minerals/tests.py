from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Testcyte"
        )
        self.assertIn(mineral, Mineral.objects.all())
        self.assertEqual(str(mineral), "Testcyte")


class MineralCatalogViewsTest(TestCase):
    def test_redirect_to_mineral_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')


class MineralViewsTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Testcyte"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={
            'pk': self.mineral.pk
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral.name, resp.context['header']['name'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.name)
