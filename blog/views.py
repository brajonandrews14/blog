from django.shortcuts import HttpResponseRedirect, render
from .models import Article, Comment
from .forms import CommentForm
from django.urls import reverse

def home(request):
    articles = Article.objects.filter(status=2).order_by('-created_at')
    context = {'articles': articles}
    return render(request, "index.html",context)


def article_detail(request, pk):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(id=pk)
            comment.save()
            return reverse('article-detail', args=[pk])

    else:
        comment_form = CommentForm()

    comments = Comment.objects.filter(article=Article.objects.get(id=pk), approved=True)

    article = Article.objects.get(id=pk)
    article.incrementViewCount()
    comment_form = CommentForm
    context = {'article': article, 'comment_form': comment_form, 'comments':comments}

    return render(request, "article_detail.html", context)