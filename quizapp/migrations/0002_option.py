# Generated by Django 3.2.9 on 2021-12-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.CharField(max_length=6)),
                ('a2', models.CharField(max_length=6)),
                ('a3', models.CharField(max_length=6)),
                ('a4', models.CharField(max_length=6)),
            ],
        ),
    ]
