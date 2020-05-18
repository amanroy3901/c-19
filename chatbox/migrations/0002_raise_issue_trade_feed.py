# Generated by Django 3.0.3 on 2020-05-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='raise_issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Raise_Id', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='trade_feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Trade', models.TextField()),
            ],
        ),
    ]
