from django.test import TestCase
from ..forms import CommentForm

from ..models import Article

class CommentFormTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="lion", hero="Covid19.jpg", content="Testing to see how this works", status=1) 

    def test_comment_form_no_article(self):
        form = CommentForm(data={"first_name": "Brajon", "last_name": "Andrews", "comment": "This is the fist comment"})
        self.assertFalse(form.is_valid())

    def test_comment_form(self):
        form = CommentForm(data={"first_name": "Brajon", "last_name": "Andrews", "article": Article.objects.get(title="lion"), "comment": "This is the fist comment"})
        self.assertTrue(form.is_valid())