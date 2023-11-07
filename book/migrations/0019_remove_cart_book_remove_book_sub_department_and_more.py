# Generated by Django 4.1.7 on 2023-11-06 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0018_alter_bookcart_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="book",
        ),
        migrations.RemoveField(
            model_name="book",
            name="sub_department",
        ),
        migrations.AddField(
            model_name="subdepartment",
            name="booklist",
            field=models.ManyToManyField(
                blank=True, related_name="booklist", to="book.book"
            ),
        ),
        migrations.AlterField(
            model_name="subdepartment",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="book.department"
            ),
        ),
        migrations.DeleteModel(
            name="BookCart",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]
