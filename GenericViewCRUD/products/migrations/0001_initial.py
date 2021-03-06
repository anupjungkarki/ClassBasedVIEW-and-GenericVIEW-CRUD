# Generated by Django 2.2.13 on 2021-01-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='product_photo')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
