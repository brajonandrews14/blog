from django.shortcuts import HttpResponseRedirect, render
from .models import Article, Comment
from .forms import CommentForm

def home(request):
    articles = Article.objects.filter(status=2).order_by('-created_at')
    context = {'articles': articles}
    return render(request, "index.html",context)


def article_detail(request, pk):

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = Article.objects.get(id=pk)
            comment.save()
            return HttpResponseRedirect( comment.article.get_absolute_url() )

    else:
        comment_form = CommentForm(initial={"article": Article.objects.get(id=pk)})

    comments = Comment.objects.filter(article=Article.objects.get(id=pk), approved=True)

    article = Article.objects.get(id=pk)
    article.incrementViewCount()
    context = {"article": article, "comment_form": comment_form, "comments":comments}

    return render(request, "article_detail.html", context)