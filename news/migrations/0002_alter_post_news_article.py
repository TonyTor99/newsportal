# Generated by Django 5.1.1 on 2024-09-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='news_article',
            field=models.CharField(choices=[('NE', 'Новости'), ('AR', 'Статья')], default='NE', max_length=2),
        ),
    ]
