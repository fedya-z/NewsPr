python manage.py shell
from django.contrib.auth.models import User
from app_name.models import Author, Category, Post, Comment

user1 = User.objects.create_user(username='Иван', password='123')
user2 = User.objects.create_user(username='Петр', password='987')

author1 = Author.objects.create(user=Иван, author_name='Author_1')
author2 = Author.objects.create(user=Петр, author_name='Author_2')

category1 = Category.objects.create(category_name='техно')
category2 = Category.objects.create(category_name='наука')
category3 = Category.objects.create(category_name='здоровье')
category4 = Category.objects.create(category_name='политика')

post1 = Post.objects.create(post_name='новые технологии', text_post='новые технологии развиваются как никогда...', author=author_1, post_type='AR')
post2 = Post.objects.create(post_name='новые лекарства', text_post='в современом мире новые лекарства появляются каждый день...', author=author_2, post_type='AR')

post3 = Post.objects.create(post_name='избран новый президент', text_post='Трамп избран президентом и помог ему в этом Маск...', author=author_1, post_type='NW')

post1.category.add(category1) 
post2.category.add(category3)
post3.category.add(category1, category4)

comment1 = Comment.objects.create(post=post1, user=Иван, comment_text='интересно')
comment2 = Comment.objects.create(post=post2, user=Петр, comment_text='не согласен')
comment3 = Comment.objects.create(post=post3, user=Иван, comment_text='так и знал')
comment4 = Comment.objects.create(post=post1, user=Петр, comment_text='есть над чем задуматься')

post1.like()
post1.like()
post2.like()
post3.dislike()

comment1.like()
comment1.like()
comment2.dislike()
comment3.like()
comment4.like()
comment4.dislike()

author1.update_rating()
author2.update_rating()

best_author = Author.objects.order_by('-rating_author').first()
print(f"Лучший пользователь: {best_author.user.username}, Рейтинг: {best_author.rating_author}")

best_post = Post.objects.order_by('-rating_post').first()
print(f"Лучшая статья:\nДата: {best_post.time_in_post}, Автор: {best_post.author.user.username}, Рейтинг: {best_post.rating_post}, Заголовок: {best_post.post_name}, Превью: {best_post.preview()}")

comments = Comment.objects.filter(post=best_post)
for comment in comments:
    print(f"Дата: {comment.time_in_comment}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating_comment}, Текст: {comment.comment_text}")
