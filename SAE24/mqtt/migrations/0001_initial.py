# Generated by Django 4.0.5 on 2022-06-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensors1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macaddr', models.CharField(max_length=12, unique=True)),
                ('piece', models.CharField(max_length=50)),
                ('emplacement', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sensors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='sensors_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('temp', models.FloatField()),
            ],
            options={
                'db_table': 'sensors_data',
                'managed': False,
            },
        ),
    ]
