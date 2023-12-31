# Generated by Django 4.2.5 on 2023-09-21 10:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='footballclub',
            options={'verbose_name': 'Футбольный клуб', 'verbose_name_plural': 'Футбольные клубы'},
        ),
        migrations.AlterModelOptions(
            name='footballer',
            options={'verbose_name': 'Футболист', 'verbose_name_plural': 'Футболисты'},
        ),
        migrations.AddField(
            model_name='footballer',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
    ]
