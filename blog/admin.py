from django.contrib import admin
from .models import Post, Comment

# Регістрація моделей у адмін панелі
admin.site.register(Post)
admin.site.register(Comment)
