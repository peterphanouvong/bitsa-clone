# Generated by Django 2.2.4 on 2019-08-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='type_of_sponsor',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
