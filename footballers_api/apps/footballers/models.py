from django.db import models

from core.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название страны')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class FootballClub(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название клуба')

    class Meta:
        verbose_name = 'Футбольный клуб'
        verbose_name_plural = 'Футбольные клубы'

    def __str__(self):
        return f'{self.name} {self.country}'


class Footballer(BaseModel):
    POSITION_CHOICES = (
        ('GK', 'Goalkeeper'),
        ('')
    )
    first_name = models.CharField(max_length=255, verbose_name='Имя', null=False, blank=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', null=False, blank=False)
    club = models.ForeignKey(FootballClub, on_delete=models.RESTRICT, verbose_name='Клуб')
    shirt_number = models.PositiveSmallIntegerField(default=0, verbose_name='Игровой номер')
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=False, null=False)

    class Meta:
        verbose_name = 'Футболист'
        verbose_name_plural = 'Футболисты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

