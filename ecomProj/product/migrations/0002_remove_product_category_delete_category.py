# Generated by Django 4.2.7 on 2024-03-27 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]