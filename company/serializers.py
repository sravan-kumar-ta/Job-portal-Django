from rest_framework import serializers

from account.serializers import UserSerializer
from company.models import Company, Job


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Company
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
