# Generated by Django 4.1 on 2022-09-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='keeptrack/default_images/default_profile_i2ejjp.png', null=True, upload_to='keeptrack/images/'),
        ),
    ]
