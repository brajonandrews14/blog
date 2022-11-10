from django.contrib import admin

from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ('title', 'created_at', 'status','viewCount')
    readonly_fields=('viewCount',)
    list_filter = ('created_at','status',)



def full_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name))
    
def approve_comments(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_comments.short_description = 'Approve Comments'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'article', 'comment', 'approved')
    search_fields = ['full_name','article', 'comment']
    actions = [approve_comments,]
    list_filter = ('approved',)





admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_header="Blog"