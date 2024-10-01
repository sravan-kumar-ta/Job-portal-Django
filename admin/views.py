from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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


class DashboardView(APIView):
    def get(self, request):
        data = User.objects.aggregate(
            job_seekers=Count('id', filter=Q(role='job_seeker')),
            companies=Count('company', distinct=True),
            jobs=Count('company__jobs', distinct=True),
            applications=Count('company__jobs__applications', distinct=True),
        )

        return Response(data, status=status.HTTP_200_OK)


class ApproveCompany(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def patch(self, request):
        company_id = request.data.get('company_id')
        is_active = request.data.get('is_active')

        if not company_id or is_active is None:
            return Response(
                {"detail": "company_id and is_active are required parameters."},
                status=status.HTTP_400_BAD_REQUEST
            )

        company = get_object_or_404(Company, id=company_id)
        company.is_active = is_active
        company.save()

        return Response({"message": "Company status updated successfully."}, status=status.HTTP_200_OK)
