# Generated by Django 4.2.13 on 2024-06-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital_app', '0007_healtheducationresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='healtheducationresource',
            name='image',
            field=models.ImageField(default=1234, upload_to='health_media'),
            preserve_default=False,
        ),
    ]
