from django.urls import path
from rest_framework.routers import DefaultRouter
from company.views import CompanyViewSet, JobViewSet, ApplicationViewSet
from company import views

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('user-company/', views.UserCompanyView.as_view()),
    path('company-jobs/', views.CompanyJobsView.as_view()),
    path('company-jobs/<int:pk>/', views.CompanyJobsView.as_view()),
] + router.urls
