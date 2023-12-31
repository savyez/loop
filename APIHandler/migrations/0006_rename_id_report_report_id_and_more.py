# Generated by Django 4.2.6 on 2023-10-21 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIHandler', '0005_rename_businesshourutcm_businesshourutc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='id',
            new_name='report_id',
        ),
        migrations.AlterUniqueTogether(
            name='storestatus',
            unique_together={('store_id', 'timestamp_utc')},
        ),
    ]
