# Generated by Django 2.2.4 on 2019-08-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190829_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/sponsor')),
                ('description', models.TextField(max_length=1000)),
                ('link', models.URLField(max_length=1000)),
            ],
        ),
    ]