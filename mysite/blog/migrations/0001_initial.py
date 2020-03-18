# Generated by Django 2.2.3 on 2019-07-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_content', models.CharField(max_length=100000)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('description_text', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]