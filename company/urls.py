from django.urls import path
from rest_framework.routers import DefaultRouter
from company.views import CompanyViewSet, JobViewSet, UserCompanyView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('user-company/', UserCompanyView.as_view()),
] + router.urls
