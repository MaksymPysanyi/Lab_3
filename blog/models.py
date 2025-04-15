from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    content = models.TextField()  # Зміст
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор
    created_at = models.DateTimeField(auto_now_add=True)  # Дата публікації
    category = models.CharField(max_length=100)  # Категорія

    def __str__(self):
        return self.title  # Повертає заголовок публікації


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Зв'язок з постом
    author = models.CharField(max_length=100)  # Автор коментаря
    content = models.TextField()  # Зміст коментаря
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення коментаря

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"  # Повертає рядок, що описує коментар
