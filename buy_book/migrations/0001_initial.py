# Generated by Django 4.1.7 on 2023-10-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('desc', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='image')),
                ('publisher', models.CharField(max_length=500)),
                ('auther', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
