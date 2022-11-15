from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Article
from django.template.defaultfilters import truncatewords

class LatestArticlesFeed(Feed):
    title = "Blog Articles"
    link = "/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Article.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content,100)

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('article-detail', args=[item.pk])