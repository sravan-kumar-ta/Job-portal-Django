from rest_framework.routers import DefaultRouter
from company.views import CompanyViewSet, JobViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = router.urls
