from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from account.serializers import UserSerializer
from admin.permissions import IsAdmin
from company.models import Company
from company.serializers import CompanySerializer

User = get_user_model()


class JobSeekersPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 50


class JobSeekersListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    pagination_class = JobSeekersPagination

    def get_queryset(self):
        return User.objects.filter(role="job_seeker").order_by('-id')


class CompaniesListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdmin]
