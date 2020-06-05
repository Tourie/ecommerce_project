# Generated by Django 3.0.6 on 2020-06-05 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('category', models.CharField(max_length=256)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('thumbnail', models.ImageField(upload_to='item_thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/shop_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField()),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.Item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Shop'),
        ),
    ]
