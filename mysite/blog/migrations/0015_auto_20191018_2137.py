# Generated by Django 2.2.4 on 2019-10-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191018_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='dummy_field',
            field=models.TextField(default='Dummy', max_length=5),
        ),
        migrations.AlterField(
            model_name='events',
            name='current_or_past',
            field=models.CharField(choices=[('CURRENT', 'Current'), ('PAST', 'Past')], default='CURRENT', max_length=250),
        ),
    ]
