# Generated by Django 4.1 on 2025-03-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_book_order_created_at_order_end_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
