from django.db import models

from ckeditor.fields import RichTextField

from core.models import BaseModel
from apps.users.models import User


class Post(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок', null=False, blank=False)
    content = RichTextField(verbose_name='Контент', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Автор')
    thumbnail = models.ImageField(verbose_name='Картинка', upload_to='news_thumbnails/', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self):
        return f'{self.title}: {self.author}'


class Comment(BaseModel):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT, verbose_name='Новость')
    title = models.CharField(verbose_name='Заголовок', max_length=255, null=False, blank=False)
    content = RichTextField(verbose_name='Контент', null=False, blank=False)

    def __str__(self):
        return f'{self.user} -> {self.post}'