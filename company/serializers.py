from django.core.exceptions import ObjectDoesNotExist
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
    company = CompanySerializer(required=False)

    class Meta:
        model = Job
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user

        try:
            company = Company.objects.get(user=user)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("The user does not have an associated company.")

        validated_data['company'] = company
        return super().create(validated_data)
