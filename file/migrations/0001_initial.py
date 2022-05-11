# Generated by Django 4.0.3 on 2022-05-10 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_remove_user_nickname'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('FileID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('isDir', models.BooleanField()),
                ('username', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
                ('fatherId', models.IntegerField(default=0)),
                ('commentFul', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('isDelete', models.BooleanField(default=False)),
                ('TeamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'File',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('CommentID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('comment_fileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.file')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]