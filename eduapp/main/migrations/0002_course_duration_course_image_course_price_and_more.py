# Generated by Django 5.0.6 on 2024-06-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=0, upload_to='Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='trainer_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
