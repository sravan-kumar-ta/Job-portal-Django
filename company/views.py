from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .permissions import IsCompanyOrAdmin
from .serializers import CompanySerializer


class CompanyViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsCompanyOrAdmin]
