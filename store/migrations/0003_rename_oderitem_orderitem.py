# Generated by Django 4.0.4 on 2022-04-30 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_customer_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
    ]