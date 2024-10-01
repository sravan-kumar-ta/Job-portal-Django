from django.urls import path

from admin import views

urlpatterns = [
    path('job-seekers/', views.JobSeekersListView.as_view()),
    path('companies/', views.CompaniesListView.as_view()),
    path('dashboard/', views.DashboardView.as_view()),
    path('company-approval/', views.ApproveCompany.as_view()),
]
