# Generated by Django 3.1.3 on 2020-12-02 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_bills_brecipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='special',
            field=models.IntegerField(default=True),
        ),
    ]
