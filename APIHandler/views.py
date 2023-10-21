import csv
import random
import datetime
from django.test import TransactionTestCase
import pandas as pd
from pytz import timezone
from rest_framework.views import APIView
from django.http import response
from rest_framework import status, generics
from .models import StoreStatus, StoreHours, StoreTimezone, Report
from .serializers import StoreStatusSerializer, ReportIdSerializer

def load_csv_to_db():
    try:
        with TransactionTestCase.atomic():
            df_stores = pd.read_csv("timezones.csv")
            df_business_hours = pd.read_csv("menu_hours.csv")
            df_store_status = pd.read_csv("store_status.csv")

            # Assuming your models have fields store_id, timezone_str, day_of_week, start_time_local, end_time_local, timestamp_utc, status
            stores = []
            business_hours = []
            store_status = []

            # Parse data from DataFrames and create model instances
            for _, row in df_stores.iterrows():
                stores.append(StoreTimezone(store_id=row['store_id'], timezone_str=row['timezone_str']))

            for _, row in df_business_hours.iterrows():
                business_hours.append(StoreHours(store_id=row['store_id'], day_of_week=row['day_of_week'], start_time_local=row['start_time_local'], end_time_local=row['end_time_local']))

            for _, row in df_store_status.iterrows():
                store_status.append(StoreStatus(store_id=row['store_id'], timestamp_utc=row['timestamp_utc'], status=row['status']))

            # Bulk create model instances
            StoreTimezone.objects.bulk_create(stores)
            StoreHours.objects.bulk_create(business_hours)
            StoreStatus.objects.bulk_create(store_status)

            return True
    except Exception as e:
        print("Error loading data to database:", e)
        return False

load_csv_to_db()

class ReportIDGenerator:
    def __init__(self):
        self.used_ids = set()

    def generate_report_id(self):
        while True:
            random_id = str(random.randint(100000, 999999))
            if random_id not in self.used_ids:
                self.used_ids.add(random_id)
                return random_id

report_id_generator = ReportIDGenerator()

class TriggerReportView(APIView):
    def post(self, request):
        # Generate report ID
        report_id = ReportIDGenerator.generate_report_id()

        # Return report ID to the user
        print(report_id)
        return response({"report_id": report_id}, status=status.HTTP_200_OK)


class GenerateReportView(APIView):
    queryset = Report.objects.all()
    serializer_class = ReportIdSerializer

    def get(self, request):
        active_stores = StoreStatus.objects.filter(status="active")
        result_data = []
        for store in active_stores:
            store_data = StoreStatus.objects.filter(store=store)
            current_time = datetime.now(timezone("UTC"))
            uptime_last_hour = store_data.filter(
                timestamp_utc__gte=current_time - datetime.timedelta(hours=1)
            ).count() * 15
            uptime_last_day = store_data.filter(
                timestamp_utc__gte=current_time - datetime.timedelta(days=1)
            ).count()
            uptime_last_week = store_data.filter(
                timestamp_utc__gte=current_time - datetime.timedelta(weeks=1)
            ).count()
            downtime_last_hour = 60 - uptime_last_hour
            downtime_last_day = 24 - uptime_last_day
            downtime_last_week = 24 * 7 - uptime_last_week
            result_data.append(
                {
                    "store_id": store.store_id,
                    "uptime_last_hour": uptime_last_hour,
                    "uptime_last_day": uptime_last_day,
                    "uptime_last_week": uptime_last_week,
                    "downtime_last_hour": downtime_last_hour * 15,
                    "downtime_last_day": downtime_last_day * 60,
                    "downtime_last_week": downtime_last_week * 60,
                }
            )
            result_df = pd.DataFrame(result_data)
            result_df.to_csv("csv\results.csv", index=False)
            return response({"message": "report generated"}, status=status.HTTP_200_OK)
