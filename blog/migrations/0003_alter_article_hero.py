# Generated by Django 3.2.15 on 2022-11-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hero',
            field=models.ImageField(upload_to=''),
        ),
    ]
