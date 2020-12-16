# Generated by Django 3.1.4 on 2020-12-16 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201215_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('temp', models.TextField()),
                ('feels_like', models.TextField()),
                ('temp_min', models.TextField()),
                ('temp_max', models.TextField()),
            ],
        ),
    ]
