# Generated by Django 4.1.2 on 2022-12-07 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0005_remove_user_medicine_time2_alter_user_medicine_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('day_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='day_id')),
                ('name', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='medicine_to_daysOfWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meds.daysofweek', verbose_name='day')),
                ('med', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meds.user_medicine', verbose_name='med')),
            ],
        ),
    ]
