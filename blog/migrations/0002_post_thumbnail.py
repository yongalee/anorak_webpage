# Generated by Django 3.0.4 on 2020-03-21 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]