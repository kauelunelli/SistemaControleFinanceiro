# Generated by Django 4.0.1 on 2022-01-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0005_delete_tipoconta_delete_tiporeceita'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoDespesa',
        ),
    ]
