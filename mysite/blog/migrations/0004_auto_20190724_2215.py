# Generated by Django 2.2.3 on 2019-07-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190724_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/static/blog/img/blog/alex.jpg', upload_to='blog/static/blog/img/blog'),
        ),
    ]
