from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from account.serializers import UserSerializer
from company.models import Company, Job, Application
from seeker.models import SeekerProfile
from seeker.serializers import SeekerProfileSerializer


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

        if not company.is_active:
            raise PermissionDenied("The company approval is pending at the Admin.")

        validated_data['company'] = company
        return super().create(validated_data)


class ApplicationSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())

    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ['applicant']

    def create(self, validated_data):
        validated_data['applicant'] = SeekerProfile.objects.get(user=self.context['request'].user)
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['job'] = JobSerializer(instance.job).data
        representation['applicant'] = SeekerProfileSerializer(instance.applicant).data
        return representation
