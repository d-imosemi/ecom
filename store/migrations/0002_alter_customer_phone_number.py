# Generated by Django 4.0.4 on 2022-04-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
