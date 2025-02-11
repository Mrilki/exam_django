from django.contrib.auth.models import User
from django.db import models

from course.models import Course


# Create your models here.

class Review(models.Model):
    rating = models.IntegerField(default=0, verbose_name = 'оценка')
    comment = models.TextField(verbose_name='комментарий')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='курс'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.comment