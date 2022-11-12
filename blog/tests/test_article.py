from django.test import TestCase
from django.urls import reverse

from ..models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="lion", hero="Covid19.jpg", content="Testing to see how this works", status=1) 

    def test_articles_link(self):
        article1  = Article.objects.get(title="lion")
        response = self.client.get(reverse('article-detail', args=[article1.pk]))
        self.assertEqual(response.status_code, 200)
