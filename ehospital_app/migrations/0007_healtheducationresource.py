# Generated by Django 4.2.13 on 2024-06-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital_app', '0006_rename_treatment_medicalhistory_allergies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthEducationResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('published_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
