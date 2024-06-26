# Generated by Django 4.2.13 on 2024-05-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital_app', '0005_remove_doctor_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='treatment',
            new_name='allergies',
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='medications',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='treatment_history',
            field=models.TextField(default=1234),
            preserve_default=False,
        ),
    ]
