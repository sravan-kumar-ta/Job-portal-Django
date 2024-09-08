from django.urls import path

from admin.views import JobSeekersListView, CompaniesListView

urlpatterns = [
    path('job-seekers/', JobSeekersListView.as_view()),
    path('companies/', CompaniesListView.as_view()),
]
