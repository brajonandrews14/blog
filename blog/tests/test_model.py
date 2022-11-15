from django.test import TestCase
from django.urls import reverse

from ..models import Article, Comment

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="lion", hero="Covid19.jpg", content="Testing to see how this works", status=1) 

    def test_articles_link(self):
        article  = Article.objects.get(title="lion")
        response = self.client.get(reverse('article-detail', args=[article.pk]))
        self.assertEqual(response.status_code, 200)

    def test_article_str(self):
        article  = Article.objects.get(title="lion")
        self.assertEqual(article.__str__(), "lion")



class CommentTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="animal", hero="Covid19.jpg", content="Testing to see how this works", status=1) 
        Comment.objects.create(first_name="Brajon", last_name="Andrews", comment="This is a test comment", article=Article.objects.get(title="animal"), approved=1)


    def test_coment_full_name(self):
        comment  = Comment.objects.get(first_name="Brajon")
        self.assertEqual(comment.full_name(), "Brajon Andrews")

