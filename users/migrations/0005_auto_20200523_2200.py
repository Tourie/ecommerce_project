# Generated by Django 3.0.6 on 2020-05-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200523_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activity',
            field=models.CharField(choices=[('Начинающий', 'Начинающий'), ('Опытный покупатель', 'Опытный покупатель')], default='Начинающий', max_length=100),
        ),
    ]
