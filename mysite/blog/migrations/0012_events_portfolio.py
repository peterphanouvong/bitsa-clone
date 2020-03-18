# Generated by Django 2.2.4 on 2019-10-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='portfolio',
            field=models.CharField(choices=[('Social', 'SOCIAL'), ('Education', 'EDUCATION'), ('Careers', 'CAREERS'), ('Creative', 'CREATIVE'), ('General', 'GENRAL')], default='GENERAL', max_length=250),
        ),
    ]