# Generated by Django 3.0.11 on 2020-11-13 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201110_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bamount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]