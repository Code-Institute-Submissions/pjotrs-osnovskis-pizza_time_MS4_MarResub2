# Generated by Django 4.0.1 on 2022-03-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_herotext_hero_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_header', models.CharField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='herotext',
            name='hero_header',
        ),
    ]
