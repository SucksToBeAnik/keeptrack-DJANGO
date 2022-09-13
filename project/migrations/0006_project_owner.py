# Generated by Django 4.1 on 2022-09-13 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_username'),
        ('project', '0005_alter_project_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]