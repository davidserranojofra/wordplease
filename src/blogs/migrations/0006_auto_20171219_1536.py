# Generated by Django 2.0 on 2017-12-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_post_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(to='blogs.Categoria'),
        ),
    ]
