from rest_framework import mixins, viewsets, generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Job
from .permissions import IsCompanyOrAdmin, IsCompany
from .serializers import CompanySerializer, JobSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsCompanyOrAdmin]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsCompanyOrAdmin]


class UserCompanyView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsCompany]

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

    def get_object(self):
        return Company.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CompanyJobsView(APIView):
    permission_classes = [IsAuthenticated, IsCompany]

    def get(self, request):
        jobs = Job.objects.filter(company__user=request.user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def patch(self, request, pk=None):
        job = Job.objects.filter(company__user=request.user, pk=pk).first()
        if not job or job.company.user != request.user:
            raise PermissionDenied("You do not have permission to update this job.")

        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
