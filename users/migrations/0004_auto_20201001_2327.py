# Generated by Django 3.1.1 on 2020-10-01 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201001_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dob',
            field=models.CharField(max_length=20),
        ),
    ]
