# Generated by Django 4.2.5 on 2023-10-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_subdepartment_subdepartment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdepartment',
            name='booklist',
            field=models.ManyToManyField(blank=True, null=True, related_name='booklist', to='book.book'),
        ),
    ]