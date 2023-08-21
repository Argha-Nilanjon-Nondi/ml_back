# Generated by Django 4.2.4 on 2023-08-18 09:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_api', '0004_customtoken_id_alter_customtoken_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='custommusic',
            name='denoised_audio_file',
            field=models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/denoised', location='/storage/emulated/0/coding/ml_back/media/denoised'), upload_to=''),
        ),
    ]
