# Generated by Django 3.0.8 on 2020-12-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slink',
            fields=[
                ('l_id', models.AutoField(primary_key=True, serialize=False)),
                ('l_name', models.CharField(max_length=100)),
            ],
        ),
    ]
