from django.urls import path
from .views import TriggerReportView, GenerateReportView

urlpatterns = [
    path('trigger_report/', TriggerReportView.as_view(), name='trigger-report'),
    path('get_reports/<str:report_id>/', GenerateReportView.as_view(), name='get-report'),
]
