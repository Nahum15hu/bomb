# Generated by Django 4.1.4 on 2022-12-07 16:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bombapp', '0002_bombsites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budapest',
            fields=[
                ('Id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(db_column='geom', srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Budapest',
                'db_table': 'budapest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hungary',
            fields=[
                ('Id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('nameHu', models.CharField(db_column='name_hu', max_length=25)),
                ('nameEn', models.CharField(db_column='name_en', max_length=25)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(db_column='geom', srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Hungary',
                'db_table': 'hungary',
                'managed': False,
            },
        ),
    ]
