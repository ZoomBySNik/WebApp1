# Generated by Django 4.1.3 on 2022-12-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_ves_product_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название компании')),
                ('adress', models.CharField(max_length=120, verbose_name='Адрес компании')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.company'),
        ),
    ]
