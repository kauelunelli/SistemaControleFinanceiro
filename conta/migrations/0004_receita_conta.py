# Generated by Django 4.0.1 on 2022-01-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0003_despesa_conta'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='conta',
            field=models.CharField(default=2, max_length=266),
            preserve_default=False,
        ),
    ]