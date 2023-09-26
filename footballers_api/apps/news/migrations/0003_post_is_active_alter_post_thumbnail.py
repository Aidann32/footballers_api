# Generated by Django 4.2.5 on 2023-09-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment_content_comment_post_comment_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news_thumbnails/', verbose_name='Картинка'),
        ),
    ]