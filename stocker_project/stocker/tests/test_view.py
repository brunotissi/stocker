from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Unidade, Insumo

#
# class ViewsTest(TestCase):
#     def test_whatever_list_view(self):
#         w = self.create_whatever()
#         url = reverse("whatever.views.whatever")
#         resp = self.client.get(url)
#
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn(w.title, resp.content)