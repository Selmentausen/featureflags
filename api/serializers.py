from rest_framework import serializers

from core.models import Environment, FeatureFlag, Organisation, Project


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = "__all__"


class FeatureFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureFlag
        fields = "__all__"
