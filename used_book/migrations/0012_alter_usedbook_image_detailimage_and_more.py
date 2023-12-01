# Generated by Django 4.2.5 on 2023-11-30 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('used_book', '0011_remove_usedbook_image_delete_photo_usedbook_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedbook',
            name='image',
            field=models.ImageField(null=True, upload_to='books/'),
        ),
        migrations.CreateModel(
            name='DetailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/images/')),
                ('used_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='used_book.usedbook')),
            ],
        ),
        migrations.AddField(
            model_name='usedbook',
            name='detail_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='used_books', to='used_book.detailimage'),
        ),
    ]