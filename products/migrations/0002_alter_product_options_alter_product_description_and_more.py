# Generated by Django 4.1.3 on 2022-11-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': ('Продукт',), 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=120, verbose_name='Название'),
        ),
    ]
