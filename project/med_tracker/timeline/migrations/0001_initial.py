# Generated by Django 4.1.2 on 2022-12-09 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meds', '0006_daysofweek_medicine_to_daysofweek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taken_medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usermed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meds.user_medicine', verbose_name='med')),
            ],
        ),
    ]
