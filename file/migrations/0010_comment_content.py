# Generated by Django 4.0.3 on 2022-05-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0009_alter_file_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]