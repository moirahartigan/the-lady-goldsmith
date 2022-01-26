# Generated by Django 3.2 on 2021-12-16 11:48

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
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254,
                                                   null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('colour', models.CharField(max_length=254)),
                ('sku', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2,
                                               max_digits=6, null=True)),
                ('pre_sale_price', models.DecimalField(blank=True,
                                                       decimal_places=2,
                                                       max_digits=6,
                                                       null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024,
                                              null=True)),
                ('image', models.ImageField(blank=True, null=True,
                                            upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.
                                               deletion.SET_NULL,
                                               to='products.category')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
