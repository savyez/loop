from rest_framework import serializers
from .models import StoreStatus, StoreHours, StoreTimezone, Report

class StoreStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreStatus
        fields = ('store_id', 'timestamp_utc', 'status')


class StoreHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreHours
        fields = ('store_id', 'day_of_week', 'start_time_local', 'end_time_local')

class StoreTimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreTimezone
        fields = ('store_id', 'timezone_str')

class ReportIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'store_id', 'timestamp_utc', 'uptime_last_hour', 'uptime_last_day',
                    'downtime_last_hour', 'downtime_last_day', 'update_last_week')