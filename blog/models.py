from django.db import models

class Article(models.Model): 
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    hero = models.ImageField(null=True, blank=True)
    content = models.TextField()
    viewCount=models.IntegerField(default=0)
    class Status(models.TextChoices):
        DRAFT = "1", "Draft"
        PUBLISHED = "2", "Published"

    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    def __str__(self):
        return self.title

    def incrementViewCount(self):
        self.viewCount += 1
        self.save()



class Comment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def full_name(self):
        return self.first_name + " " + self.last_name