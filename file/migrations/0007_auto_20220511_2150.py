# Generated by Django 3.2.12 on 2022-05-11 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_rename_fatherid_file_fatherid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='teamID',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='userID',
            new_name='user',
        ),
    ]