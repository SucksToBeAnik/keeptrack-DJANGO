# Generated by Django 4.1 on 2022-09-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0010_alter_skillobj_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
