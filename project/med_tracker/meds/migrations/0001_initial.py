# Generated by Django 4.1.2 on 2022-12-07 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Med_type',
            fields=[
                ('med_typeID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='type_id')),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]