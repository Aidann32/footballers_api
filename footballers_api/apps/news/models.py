from core.models import BaseModel
from apps.users.models import User

from ckeditor.fields import RichTextField


class Post(BaseModel):
    # title = models.CharField(max_length=255, verbose_name='Заголовок', null=False, blank=False)
    # content = RichTextField()
    # author = models.ForeignKey(User, on_delete=models.RESTRICT)

    # def __str__(self):
    #     return f'{self.title}: {self.author}'
    pass


class Comment(BaseModel):
    pass