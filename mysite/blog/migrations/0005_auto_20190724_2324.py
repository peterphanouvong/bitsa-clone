# Generated by Django 2.2.3 on 2019-07-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190724_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
