# Generated by Django 3.1.1 on 2020-10-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201029_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bamount',
            field=models.CharField(max_length=20),
        ),
    ]