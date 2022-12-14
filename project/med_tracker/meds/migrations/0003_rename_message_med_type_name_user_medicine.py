# Generated by Django 4.1.2 on 2022-12-07 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meds', '0002_alter_med_type_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='med_type',
            old_name='message',
            new_name='name',
        ),
        migrations.CreateModel(
            name='User_Medicine',
            fields=[
                ('usermed_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='med_id')),
                ('name', models.CharField(max_length=1000, null=True)),
                ('time', models.CharField(max_length=1000, null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meds.med_type', verbose_name='type')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'db_table': 'User_Medicine',
            },
        ),
    ]
