from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Article, Comment
from ..forms import CommentForm

class ArticleDetailTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="lion", hero="Covid19.jpg", content="Testing to see how this works", status=1) 
        self.client = Client()
        self.article_detail_url = reverse('article-detail', args=[1])

    def test_detail_view_GET(self):
        response = self.client.get(self.article_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertContains( response, 'There are no approved comments for this article')

    def test_detail_view_POST(self):
        article = Article.objects.get(title="lion")
        self.client.post(self.article_detail_url, {"first_name": "Brajon", "last_name": "Andrews", "article": article.id, "comment": "This is the fist comment"})

        self.assertTrue(Comment.objects.filter(first_name='Brajon').exists())
