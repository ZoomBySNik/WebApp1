# Generated by Django 4.1.3 on 2022-11-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ves',
            field=models.TextField(blank=True, verbose_name='Вес'),
        ),
    ]