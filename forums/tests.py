from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_forums


class TestForumIndex(TestCase):
    def test_forum_index_uses_the_correct_template(self):
        response = self.client.get('/forums/')
        self.assertTemplateUsed(response, 'index.html')

    def test_forum_root_url_resolves_to_homepage(self):
        page = resolve('/forums/')
        self.assertEqual(home_forums, page.func)
