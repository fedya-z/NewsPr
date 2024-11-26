from django.contrib import admin
from .models import Post, User, Author, Category, PostCategory, Comment


admin.site.register(Post)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
