# Generated by Django 3.0.5 on 2020-05-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(max_length=200)),
            ],
        ),
    ]
