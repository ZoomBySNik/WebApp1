# Generated by Django 4.1.7 on 2023-04-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_company_options_alter_productinstance_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.TextField(blank=True, null=True, verbose_name='Вес'),
        ),
    ]