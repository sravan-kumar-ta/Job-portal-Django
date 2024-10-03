from django.urls import path

from admin import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view()),
    path('job-seekers/', views.JobSeekersListView.as_view()),
    path('companies/', views.CompaniesListView.as_view()),
    path('company-approval/', views.ApproveCompany.as_view()),
    path('jobs/', views.AllJobsListView.as_view()),
    path('applications/', views.AllApplicationListView.as_view()),
]
