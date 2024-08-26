from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated

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