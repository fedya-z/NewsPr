from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=255)

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    rating_author = models.FloatField(default=0.0)

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def update_rating(self):
        posts_rating = self.post_set.aggregate(total=models.Sum('rating_post'))['total'] or 0
        posts_rating *= 3

        comments_rating = self.user.comment_set.aggregate(total=models.Sum('rating_comment'))['total'] or 0

        comments_on_posts_rating = Comment.objects.filter(post__author=self).aggregate(
            total=models.Sum('rating_comment')
        )['total'] or 0

        self.rating_author = posts_rating + comments_rating + comments_on_posts_rating
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique = True)


class Post(models.Model):
    ARTICLE = 'AR'
    NEWS = 'NW'
    POST_TYPE_CHOICES = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость'),
    ]
    post_name = models.CharField(max_length=255)
    text_post = models.CharField()
    rating_post = models.FloatField(default=0.0)
    time_in_post = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField( max_length=2,choices=POST_TYPE_CHOICES,default=ARTICLE,)

    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[:124] + '...' if len(self.text_post) > 124 else self.text_post
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    time_in_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()