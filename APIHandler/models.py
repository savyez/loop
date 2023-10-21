from django.db import models

class StoreStatus(models.Model):
    store_id = models.IntegerField(primary_key=True)
    timestamp_utc = models.DateTimeField()
    status = models.CharField(max_length=10)

    class Meta:
        unique_together = ('store_id', 'timestamp_utc')


class StoreHours(models.Model):
    store_id = models.IntegerField(primary_key=True)
    day_of_week = models.IntegerField()  # 0=Monday, 6=Sunday
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

class StoreTimezone(models.Model):
    store_id = models.IntegerField(primary_key=True)
    timezone_str = models.CharField(max_length=50)  # Timezone string, e.g., 'America/Chicago'

class BusinessHour(models.Model):
    store_id = models.IntegerField(primary_key=True)
    day_of_week =models.IntegerField()
    start_time_local = models.DateTimeField()
    end_time_local = models.DateTimeField()

class BusinessHourUTC(models.Model):
    store_id = models.IntegerField(primary_key=True)
    day_of_week =models.IntegerField()
    start_time_local = models.DateTimeField()
    end_time_local = models.DateTimeField()
    start_time_utc = models.DateTimeField()
    end_time_utc = models.DateTimeField()

class Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField(null=False)
    timestamp_utc = models.DateTimeField(null=False)
    uptime_last_hour = models.IntegerField()
    uptime_last_day = models.IntegerField()
    downtime_last_hour = models.IntegerField()
    downtime_last_day = models.IntegerField()
    update_last_week = models.IntegerField()
