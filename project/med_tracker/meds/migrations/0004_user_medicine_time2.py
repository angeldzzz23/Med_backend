# Generated by Django 4.1.2 on 2022-12-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0003_rename_message_med_type_name_user_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_medicine',
            name='time2',
            field=models.TimeField(null=True),
        ),
    ]