# Generated by Django 4.1.2 on 2023-03-22 09:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image1', models.ImageField(upload_to='gallery')),
                ('product_image2', models.ImageField(upload_to='gallery')),
                ('product_image3', models.ImageField(upload_to='gallery')),
                ('product_image4', models.ImageField(upload_to='gallery')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.IntegerField(default=0)),
                ('product_offer', models.IntegerField(default=0)),
                ('product_description', ckeditor.fields.RichTextField()),
                ('select_category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
