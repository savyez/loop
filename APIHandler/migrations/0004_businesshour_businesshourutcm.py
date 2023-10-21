# Generated by Django 4.2.6 on 2023-10-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIHandler', '0003_report_remove_storehours_id_remove_storestatus_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('day_of_week', models.IntegerField()),
                ('start_time_local', models.DateTimeField()),
                ('end_time_local', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BusinessHourUTCm',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('day_of_week', models.IntegerField()),
                ('start_time_local', models.DateTimeField()),
                ('end_time_local', models.DateTimeField()),
                ('start_time_utc', models.DateTimeField()),
                ('end_time_utc', models.DateTimeField()),
            ],
        ),
    ]