# Generated by Django 4.2.13 on 2024-05-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
